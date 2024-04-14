import numpy as np
from osgeo import gdal, gdalconst, gdal_array
import os, glob


def ResamplerBatch(maskTif, tifFiles, output_folder=None):
    match_ds = gdal.Open(maskTif, gdalconst.GA_ReadOnly)
    match_proj = match_ds.GetProjection()
    match_geotrans = match_ds.GetGeoTransform()
    wide = match_ds.RasterXSize
    high = match_ds.RasterYSize
    data_type = {
        0: gdalconst.GDT_Unknown,
        1: gdalconst.GDT_Byte,
        2: gdalconst.GDT_UInt16,
        3: gdalconst.GDT_Int16,
        4: gdalconst.GDT_UInt32,
        5: gdalconst.GDT_Int32,
        6: gdalconst.GDT_Float32,
        7: gdalconst.GDT_Float64,
        8: gdalconst.GDT_CInt16,
        9: gdalconst.GDT_CInt32,
        10: gdalconst.GDT_CFloat32,
        11: gdalconst.GDT_CFloat64
    }
    if output_folder is not None:
        for tifFile in tifFiles:
            src_tiffName = os.path.basename(tifFile)
            src = gdal.Open(tifFile, gdalconst.GA_ReadOnly)
            band = src.GetRasterBand(1)
            A = band.DataType
            src_proj = src.GetProjection()
            src_geotrans = src.GetGeoTransform()
            dst_tiffName = os.path.join(output_folder, src_tiffName[0:-4] + "_resample" + ".tif")
            dst = gdal.GetDriverByName('GTiff').Create(dst_tiffName, wide, high, 1, data_type[A])
            dst.SetGeoTransform(match_geotrans)
            dst.SetProjection(match_proj)
            dst.GetRasterBand(1).SetNoDataValue(-9999)
            gdal.ReprojectImage(src, dst, src_proj, match_proj, gdalconst.GRA_Bilinear)
            del dst
        return None
    else:
        resampled_data_list = []
        for tifFile in tifFiles:
            src = gdal.Open(tifFile, gdalconst.GA_ReadOnly)
            src_proj = src.GetProjection()
            src_geotrans = src.GetGeoTransform()
            dst = gdal.GetDriverByName('MEM').Create('', wide, high, 1, gdalconst.GDT_Float32)
            dst.SetGeoTransform(match_geotrans)
            dst.SetProjection(match_proj)
            dst.GetRasterBand(1).SetNoDataValue(-9999)
            gdal.ReprojectImage(src, dst, src_proj, match_proj, gdalconst.GRA_Bilinear)
            resampled_data = dst.ReadAsArray()  # 读取重采样后的数据
            resampled_data_list.append(resampled_data)
        return np.stack(resampled_data_list, axis=-1)
