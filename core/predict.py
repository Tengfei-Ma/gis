import os, glob
import numpy as np
from osgeo import gdal
from .train import getTiffDataFromTiffFiles
import joblib
from scipy.io import savemat




def useModelPredict(tiffData, Trainedmodel, row, col):
    ArrayLabels = np.full([row, col], np.nan)
    for ii in np.arange(0, row):
        ImageHangData = tiffData[ii, :, :]
        ImageHangPathes = []
        for kk in np.arange(0, col):
            Imageonepath = ImageHangData[:, kk: kk + 1, :]
            ImageHangPathes.append(Imageonepath.flatten())
        HangResult = Trainedmodel.predict(np.array(ImageHangPathes))
        ArrayLabels[ii, :] = HangResult.flatten()
    return ArrayLabels


def UseModelToMapping(ArrayLabels, modelPath, Model_name, in_geo_ds):
    Mean_ArrayLabels = np.nanmean(ArrayLabels, axis=2)
    # P95_ArrayLabels = np.nanpercentile(ArrayLabels, 95, axis=2)
    # P5_ArrayLabels = np.nanpercentile(ArrayLabels, 5, axis=2)
    # Uncertainty_Standard = (P95_ArrayLabels - P5_ArrayLabels) / Mean_ArrayLabels

    TiffResultPath = modelPath + '\\tiffresult\\'
    if not os.path.exists(TiffResultPath):  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(TiffResultPath)
    Mean_ArrayLabels_fn = os.path.join(TiffResultPath, Model_name + "_" + "Mean_Array" + ".tif")
    # P95_ArrayLabels_fn = os.path.join(TiffResultPath, Model_name + "_" + "P95_Array" + ".tif")
    # P5_ArrayLabels_fn = os.path.join(TiffResultPath, Model_name + "_" + "P5_Array" + ".tif")
    # Uncertainty_Standard_fn = os.path.join(TiffResultPath, Model_name + "_" + "Uncertainty_Standard_Array" + ".tif")
    # CV_ArrayLabels_fn = os.path.join(TiffResultPath, Model_name + "_" + "CV_Array" + ".tif")

    make_raster(in_geo_ds, Mean_ArrayLabels_fn, Mean_ArrayLabels, gdal.GDT_Float32, nodata=-9999)
    # make_raster(in_geo_ds, P95_ArrayLabels_fn, P95_ArrayLabels, gdal.GDT_Float32, nodata=-9999)
    # make_raster(in_geo_ds, P5_ArrayLabels_fn, P5_ArrayLabels, gdal.GDT_Float32, nodata=-9999)
    # make_raster(in_geo_ds, Uncertainty_Standard_fn, Uncertainty_Standard,  gdal.GDT_Float32, nodata=-9999)
    print("=" * 20, '结果已写入TIFF数据', "=" * 20)


def make_raster(in_ds, fn, data, data_type, nodata=None):
    """Create a one-band GeoTIFF.

        in_ds     - datasource to copy projection and geotransform from
        fn        - path to the file to create
        data      - NumPy array containing data to write
        data_type - output data type
        nodata    - optional NoData value
    """
    driver = gdal.GetDriverByName('GTiff')
    out_ds = driver.Create(
        fn, in_ds.RasterXSize, in_ds.RasterYSize, 1, data_type)
    out_ds.SetProjection(in_ds.GetProjection())
    out_ds.SetGeoTransform(in_ds.GetGeoTransform())
    out_band = out_ds.GetRasterBand(1)
    if nodata is not None:
        out_band.SetNoDataValue(nodata)
    out_band.WriteArray(data)
    out_band.FlushCache()
    out_band.ComputeStatistics(False)
    return out_ds


if __name__ == '__main__':
    modelPath = ""
    TrainedModel_path = sorted(glob.glob(os.path.join(modelPath, '*.pkl')))

    tiffFiles = []

    tiffData = getTiffDataFromTiffFiles(tiffFiles)
    row = tiffData.shape[0]
    col = tiffData.shape[1]
    ArrayLabels = np.full([row, col, 10], np.nan)
    for i in range(2):
        SingleTrainedModel = joblib.load(TrainedModel_path[i])
        print(TrainedModel_path[i])
        singleArrayLabel = useModelPredict(tiffData, SingleTrainedModel, row, col)
        ArrayLabels[:, :, i] = singleArrayLabel
        matResultPath = TrainedModel_path[i] + '.mat'
        savemat(matResultPath, {'value': singleArrayLabel})
    print("=" * 20, '预测结果均写入三维数组', "=" * 20)

    in_geo_ds = gdal.Open(tiffFiles[0])
    UseModelToMapping(ArrayLabels, modelPath, "RF", in_geo_ds)
