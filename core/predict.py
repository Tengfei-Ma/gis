import os, glob
import numpy as np
from osgeo import gdal
from .train import getTiffDataFromTiffFiles
import joblib
from scipy.io import savemat
from core.resample import ResamplerBatch


def UseModelToMapping(ArrayLabels, targetTifDir, field_name, in_geo_ds):
    if ArrayLabels.shape[2] > 1:
        labels = np.nanmean(ArrayLabels, axis=2)
    else:
        labels = ArrayLabels.squeeze()
    Mean_ArrayLabels_fn = os.path.join(targetTifDir, field_name + "_final.tif")
    make_raster(in_geo_ds, Mean_ArrayLabels_fn, labels, gdal.GDT_Float32, nodata=-9999)


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


def predictTif(tifFiles, modelFiles, maskTifFile, targetTifDir, progressbar):
    try:
        tiffData = ResamplerBatch(maskTifFile, tifFiles)
        row = tiffData.shape[0]
        col = tiffData.shape[1]
        ArrayLabels = np.full([row, col, len(modelFiles)], np.nan)
        total_progress = len(modelFiles) * row
        progress = 0
        for i in range(len(modelFiles)):
            model = joblib.load(modelFiles[i])
            labels = np.full([row, col], np.nan)
            for ii in np.arange(0, row):
                progress += 1
                progressbar.setValue((progress / total_progress) * 100)
                data = tiffData[ii, :, :]
                HangResult = model.predict(data)
                labels[ii, :] = HangResult.flatten()
            ArrayLabels[:, :, i] = labels
            matResultPath = modelFiles[i][:-4] + '.mat'
            savemat(matResultPath, {'value': labels})

        in_geo_ds = gdal.Open(maskTifFile)
        UseModelToMapping(ArrayLabels, targetTifDir, os.path.basename(os.path.dirname(modelFiles[0])), in_geo_ds)
    except Exception as e:
        return [0, e]
    else:
        return [1, "预测结束，目标tif已保存至指定目录！"]
