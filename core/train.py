import os
import math
from datetime import datetime
import pandas as pd
import joblib
import geopandas as gpd
import numpy as np
from osgeo import ogr, gdal
from skimage import io
from .model import build
from sklearn.model_selection import train_test_split

from .metric import ccc, me
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

model_dict = {
    0: "RF",
    1: "SVM",
    2: "XGBoost"
}


def xy2rowCol(dataset, x, y):
    """
    根据GDAL的六参数模型将给定的投影或地理坐标转为行列号
    :param dataset: GDAL地理数据
    :param x: 投影或地理坐标x
    :param y: 投影或地理坐标y
    :return: 影坐标或地理坐标(x, y)对应的影像图上行列号(row, col)
    """
    trans = dataset.GetGeoTransform()
    a = np.array([[trans[1], trans[2]], [trans[4], trans[5]]])
    b = np.array([x - trans[0], y - trans[3]])
    return np.linalg.solve(a, b)  # 使用numpy的linalg.solve进行二元一次方程的求解


def getRowsCols(tiffPath, shpPath):
    """
    获取shp文件中的点在tiff中的行列号
    :param tiffPath: tiff文件路径
    :param shpPath: shp文件路径
    :return: 行列号
    """

    ogr.RegisterAll()  # 注册驱动
    datasource = ogr.Open(shpPath, 0)  # 以只读模式打开文件
    lyr = datasource.GetLayer(0)  # 打开shp文件的第一个图层
    DSpan = gdal.Open(tiffPath)
    rowsCols = []
    for feat in lyr:  # for循环遍历shp第一个图层的所有要素（这里是样点）
        pt = feat.geometry()  # 从要素中获得几何形状（即点、线、面）
        tempRowCol = xy2rowCol(DSpan, pt.GetX(), pt.GetY())
        Row = int(math.floor(tempRowCol[1]))
        Col = int(math.floor(tempRowCol[0]))
        rowsCols.append([Row, Col])
    return rowsCols


def getLabels(shpPath, field):
    ogr.RegisterAll()  # 注册驱动
    datasource = ogr.Open(shpPath, 0)  # 以只读模式打开文件
    lyr = datasource.GetLayer(0)  # 打开shp文件的第一个图层
    labels = []
    for feat in lyr:  # for循环遍历shp第一个图层的所有要素（这里是样点）
        label = feat.GetField(field)  # 从shp文件指标的字段中获取标签值
        labels.append(np.float64(label))
    return np.array(labels)


def makeSample(tiffData, rowsCols):
    """

    :param tiffData: 读入的tiff数据
    :param rowsCols: 点的行列号
    :param labels: 点对应的标签
    :return:
    """
    row = tiffData.shape[0]
    col = tiffData.shape[1]
    AllXdata = tiffData.reshape(row * col, 1)
    SampleIndex = []
    for temp in rowsCols:
        SampleIndex.append(temp[0] * col + temp[1])
    sample_feature = AllXdata[SampleIndex, :]
    return sample_feature.squeeze()


def getFieldsFromShp(shpPath):
    """
    根据shp文件获取可选择字段
    :param shpPath: shp文件路径
    :return: 可选择字段
    """
    ogr.RegisterAll()  # 注册驱动
    datasource = ogr.Open(shpPath, 0)  # 以只读模式打开文件
    lyr = datasource.GetLayer(0)  # 打开shp文件的第一个图层
    layer_defn = lyr.GetLayerDefn()
    fields = []
    for i in range(layer_defn.GetFieldCount()):
        field_defn = layer_defn.GetFieldDefn(i)
        fields.append(field_defn.GetName())
    return fields


def TrainAndTest(model, sampleFeatures, sampleLabels, valRatio, seed):
    """
    提供随机种子训练并测试模型
    :param model: 选用模型
    :param sampleFeatures: 样本特征数组
    :param sampleLabels: 样本标签
    :param seed: 随机种子
    :return: 返回以下指标
             ME: 平均误差
             MAE: 平均绝对误差
             RMSE: 均方根误差
             R2: 决定系数
             LCCC: 线性一致性相关系数
    """
    train_X, test_X, train_Y, test_Y = train_test_split(sampleFeatures, sampleLabels, test_size=valRatio,
                                                        random_state=seed)
    model.fit(train_X, train_Y)
    test_pre_Y = model.predict(test_X)
    val_ME = me(test_Y, test_pre_Y)
    val_MAE = mean_absolute_error(test_Y, test_pre_Y)
    val_RMSE = np.sqrt(mean_squared_error(test_Y, test_pre_Y))
    val_R2 = r2_score(test_Y, test_pre_Y)
    val_LCCC = ccc(test_Y, test_pre_Y)

    train_pre_Y = model.predict(train_X)
    train_ME = me(train_Y, train_pre_Y)
    train_MAE = mean_absolute_error(train_Y, train_pre_Y)
    train_RMSE = np.sqrt(mean_squared_error(train_Y, train_pre_Y))
    train_R2 = r2_score(train_Y, train_pre_Y)
    train_LCCC = ccc(train_Y, train_pre_Y)

    return val_ME, val_MAE, val_RMSE, val_R2, val_LCCC, train_ME, train_MAE, train_RMSE, train_R2, train_LCCC, model


def getTiffDataFromTiffFiles(tiffFiles):
    """
    将重采样后c个h*w的的tiff文件拼接成h*w*c的数组返回
    :param tiffFiles:输入行列一致的tif文件绝对路径列表
    :return:h*w*c的tiff数组
    """
    tiff_arrays = []
    for e in tiffFiles:
        data = io.imread(e)
        tiff_arrays.append(data)
    return np.stack(tiff_arrays, axis=-1)


def trainShp(shpPath, tifFiles, tasks, modelIndex, modelArgs, valRatio, trainTimes, k, modelDir, progressbar):
    try:
        taskPath = os.path.join(modelDir, f'exp_{datetime.now().strftime("%y%m%d_%H%M")}')
        total_progress = len(tasks) * trainTimes
        progress = 0;
        for task in tasks:
            modelPath = os.path.join(taskPath, task)
            os.makedirs(modelPath, exist_ok=True)
            # 根据shp文件得到标签Y
            labels = getLabels(shpPath, task)  # shp文件所有点对应字段的标签
            feature_list = []
            feature_name = []
            for tifFile in tifFiles:
                feature_name.append(os.path.basename(tifFile)[:-4])
                tiffData = io.imread(tifFile)
                rowsCols = getRowsCols(tifFile, shpPath)
                sampleFeature = makeSample(tiffData, rowsCols)
                feature_list.append(sampleFeature)
            sampleFeatures = np.stack(feature_list, axis=-1)
            # 选择机器学习算法
            model = build(modelIndex, modelArgs)
            val_score_list = []
            train_score_list = []
            name = ["model_name", "ME", "MAE", "RMSE", "R2", "LCCC"]
            val_score_list.append(name)
            train_score_list.append(name)
            topK_model_dict = {}
            seed_dict = {}
            for i in range(trainTimes):
                progress += 1
                progressbar.setValue((progress / total_progress) * 100)
                seed = i * 500 + 200  # 随意给的数值，为了保证在每次循环中，所有模型的训练集和验证集划分情况一致
                val_ME, val_MAE, val_RMSE, val_R2, val_LCCC, train_ME, train_MAE, train_RMSE, train_R2, train_LCCC, model = TrainAndTest(
                    model, sampleFeatures, labels, valRatio, seed)
                model_name = model_dict[modelIndex] + '_' + str(i + 1).zfill(2)
                val_score_list.append([model_name, val_ME, val_MAE, val_RMSE, val_R2, val_LCCC])
                train_score_list.append([model_name, train_ME, train_MAE, train_RMSE, train_R2, train_LCCC])
                topK_model_dict[model_name] = model
                seed_dict[model_name] = seed
            sort_score_list = sorted(val_score_list[1:], key=lambda x: x[4], reverse=True)
            for i in range(k):
                top_model = topK_model_dict[sort_score_list[i][0]]
                joblib.dump(top_model, os.path.join(modelPath, sort_score_list[i][0] + ".pkl"))
                otherPath = os.path.join(modelPath, "other_top_" + str(i+1))
                os.makedirs(otherPath, exist_ok=True)

                importances = top_model.feature_importances_
                indices = np.argsort(importances)[::-1]
                result_list = []
                for i in range(sampleFeatures.shape[1]):
                    result_list.append((feature_name[indices[i]], importances[indices[i]]))
                result_array = np.array(result_list)
                data = pd.DataFrame(result_array, columns=['Environment variables', 'Relative importance'])
                excelPath = os.path.join(otherPath, "relative_importance.xlsx")
                with pd.ExcelWriter(excelPath) as writer:
                    data.to_excel(writer, 'importance', float_format='%.5f')

                gdf = gpd.read_file(shpPath)
                train_id, test_id, train_X, test_X, train_Y, test_Y = train_test_split(gdf.index, sampleFeatures,
                                                                                       labels,
                                                                                       test_size=valRatio,
                                                                                       random_state=seed_dict[
                                                                                           sort_score_list[i][0]])
                train_gdf = gdf[gdf.index.isin(train_id)]
                test_gdf = gdf[gdf.index.isin(test_id)]
                train_gdf.to_file(os.path.join(otherPath, "train_data.shp"))
                test_gdf.to_file(os.path.join(otherPath, "test_data.shp"))
            val_CSV_filename = modelPath + r'\val_score.csv'
            data = np.array(val_score_list, dtype=str)
            np.savetxt(val_CSV_filename, data, delimiter=",", fmt='%s')
            train_CSV_filename = modelPath + r'\train_score.csv'
            data = np.array(train_score_list, dtype=str)
            np.savetxt(train_CSV_filename, data, delimiter=",", fmt='%s')
    except Exception as e:
        print(e)
        return 0
    else:
        return 1
