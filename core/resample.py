from osgeo import gdal, gdalconst
import os, glob


def ResampleRasterBatch(match_filename, input_srcfolder, output_dstfolder):
    """
    将tiff重采样到统一大小
    :param match_filename: 采样最终tiff文件的大小
    :param input_srcfolder: 输入tiff文件的文件夹路径
    :param output_dstfolder: 输出tiff文件的文件夹路径
    """
    match_ds = gdal.Open(match_filename, gdalconst.GA_ReadOnly)
    match_proj = match_ds.GetProjection()
    match_geotrans = match_ds.GetGeoTransform()
    wide = match_ds.RasterXSize
    high = match_ds.RasterYSize

    input_path = sorted(glob.glob(os.path.join(input_srcfolder, '*.tif')))
    lenth = len(input_path)
    for i in range(lenth):
        src_tiffName = [os.path.basename(x) for x in glob.glob(input_path[i])]
        src_tiff = input_path[i]
        print(src_tiff)
        src = gdal.Open(src_tiff, gdalconst.GA_ReadOnly)
        src_proj = src.GetProjection()
        src_geotrans = src.GetGeoTransform()
        # Output / destination
        dst_tiffName = os.path.join(output_dstfolder, src_tiffName[0][0:-4] + "_resample" + ".tif")
        dst = gdal.GetDriverByName('GTiff').Create(dst_tiffName, wide, high, 1, gdalconst.GDT_Float32)
        dst.SetGeoTransform(match_geotrans)
        dst.SetProjection(match_proj)
        dst.GetRasterBand(1).SetNoDataValue(-9999)  # ！！！！

        # Do the work
        gdal.ReprojectImage(src, dst, src_proj, match_proj, gdalconst.GRA_Bilinear)

        del dst  # Flush


if __name__ == '__main__':
    input_srcfolder = r'F:\gis\input'
    output_dstfolder = r'F:\gis\output'
    match_filename = r'F:\gis\tif\Ele\Eletemp.tif'
    ResampleRasterBatch(match_filename, input_srcfolder, output_dstfolder)
