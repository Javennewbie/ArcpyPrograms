# -*- coding:utf-8 -*-

import arcpy
import sys

sys.path.append('DataProcess/Py/')
sys.path.append('ArcpyToImage/')

# from getCentroid import get_centroid
# from csTrans import project_to_wgs84, wgs84_to_project
from getArea import get_area
# from arcCpm import get_choropleth_map
from arcXYLine import get_xy_line

# shp1 = r'E:\Desktop\202301\202303\上海\上海街道镇\杨浦街道.shp'
# shp2 = r'E:\Desktop\202301\202303\上海\上海街道镇\杨浦街道_pro.shp'
# lon = 121
# # project_to_wgs84(shp1, shp2)
# wgs84_to_project(shp1, shp2, lon)

# shp = r'E:\Desktop\202301\202303\上海\小区\TAZ_Pro.shp'
# primary_key = 'ID'
# out_location = r'E:\Desktop\202301\202303\上海\小区'
# out_table_name = 'shanghai_taz_cenXY_P'
# get_centroid(shp, primary_key, out_location, out_table_name, label='zh')

# shp = r'E:\Desktop\ArcpyPrograms\ArcpyToImage\MapDocuments\ShaanXi\ShaanXi.shp'
# out_location = r'E:\Desktop\ArcpyPrograms\ArcpyToImage\DataBasic\Data'
# primary_key = 'id'
# out_table_name = 'shaanxi_xy'
# # label 中文路径为zh 英文路径为en
# get_centroid(shp, primary_key, out_location, out_table_name, label='en')


# shp = r'E:\Desktop\202301\202303\上海\上海街道镇\杨浦街道_pro.shp'
# get_area(shp)


# Choroplethmap
# shp_path = r'E:\Desktop\ArcpyPrograms\ArcpyToImage\MapDocuments\ShaanXi\ShaanXi.shp'
# data_path = r'E:\Desktop\ArcpyPrograms\ArcpyToImage\DataBasic\Data\PopulationData'
# my_lyr_path = r'E:\Desktop\ArcpyPrograms\ArcpyToImage\DataBasic\TemplateFiles\choropleth.lyr'
# mxd_path = r'E:\Desktop\ArcpyPrograms\ArcpyToImage\DataBasic\Mxd\choropleth.mxd'
# png_path = r'E:\Desktop\ArcpyPrograms\ArcpyToImage\ResData\PNG'
# join_field1 = "id"
# join_field2 = 'NAME'
# cal_field1 = 'Area'
# cal_field2 = 'COUNT'
# res_field = 'res'
# get_choropleth_map(shp_path, data_path, my_lyr_path, mxd_path, png_path, join_field1,
#                    join_field2, cal_field1, cal_field2, res_field)


# get_XYToLine
min_value = 0
city_xy_path = r'E:\Desktop\ArcpyPrograms\1\village_xy.csv'
city_od_path = r'E:\Desktop\202301\万州\0412_pic\data\od_data\village'
city_od_output_path = r'E:\Desktop\202301\万州\0412_pic\data\od_data_out'
city_odline_output_path = r'E:\Desktop\202301\万州\0412_pic\data\od_line'
my_lyr_path = r'E:\Desktop\202301\万州\0412_pic\lyr\line_model.lyr'
mxd_path = r"E:\Desktop\202301\万州\0412_pic\mxd\village.mxd"
png_path = r'E:\Desktop\202301\万州\0412_pic\output\img'
code_format = 'gbk'

get_xy_line(code_format, min_value, city_xy_path, city_od_path, city_od_output_path,
            city_odline_output_path, mxd_path, my_lyr_path, png_path)
