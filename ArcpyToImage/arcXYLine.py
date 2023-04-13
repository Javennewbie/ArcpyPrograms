# -*- coding:utf-8 -*-

import arcpy
import os
import sys
import pandas as pd

# 添加中文支持
reload(sys)
sys.setdefaultencoding('utf8')
arcpy.env.overwriteOutput = True


def get_xy_line(code_format, min_value, city_xy_path, city_od_path, city_od_output_path,
                city_odline_output_path, mxd_path, my_lyr_path, png_path):
    xy = pd.read_csv(city_xy_path, encoding=code_format)
    xy.columns = ['city', 'x', 'y']
    for od_file in os.listdir(city_od_path.encode("gbk").decode("utf-8")):
        city_od_name = os.path.basename(od_file).split('.')[0]
        city_od = city_od_path + '\\' + od_file
        od = pd.read_csv(city_od, encoding=code_format)
        new_od_xy = pd.DataFrame(columns=['city_o', 'x_o', 'y_o', 'city_d', 'x_d', 'y_d', 'cov'])
        xy_dict = xy.set_index('city').to_dict('dict')
        xx = xy_dict['x']
        yy = xy_dict['y']
        for item in od.iterrows():
            city_o = item[1][0]
            city_d = item[1][1]
            if city_o in xx.keys() and city_d in xx.keys() and city_o in yy.keys() and city_d in yy.keys() \
                    and city_o != city_d:
                x_o = xx[city_o]
                y_o = yy[city_o]
                x_d = xx[city_d]
                y_d = yy[city_d]
                new_od_xy = new_od_xy.append(
                    {'city_o': city_o, 'x_o': x_o, 'y_o': y_o, 'city_d': city_d, 'x_d': x_d, 'y_d': y_d, 'cov': item[1][2]},
                    ignore_index=True)
        new_od_xy = new_od_xy[new_od_xy['cov'] >= min_value]
        new_od_xy = new_od_xy.sort(['cov'])
        new_od_xy.to_csv(city_od_output_path + '\\' + city_od_name + '.csv', encoding=code_format, index=False)

    str1 = ' 人次'
    # dict_key = {'周末常住人口出行量分布': 'weekend_cz', '工作日常住人口出行量分布': 'workday_cz',}

    for od_out_file in os.listdir(city_od_output_path.encode("gbk").decode("utf-8")):
        od_to_display = city_od_output_path + '\\' + od_out_file
        png_name = os.path.basename(od_out_file).split('.')[0]
        # mxd_name = dict_key[str(png_name)]

        my_lyr = arcpy.mapping.Layer(my_lyr_path)
        mxd = arcpy.mapping.MapDocument(mxd_path)

        input_table = od_to_display
        out_lines = city_odline_output_path + '\\' + png_name + '.shp'
        arcpy.XYToLine_management(input_table, out_lines, "x_o", "y_o", "x_d", "y_d", "GEODESIC", "cov")

        df = arcpy.mapping.ListDataFrames(mxd)[0]
        add_layer = arcpy.mapping.Layer(out_lines)
        arcpy.mapping.AddLayer(df, add_layer, "TOP")
        # mxd.saveACopy(r"C:\Users\QC7\Documents\ArcGIS\arcpyProjects\data\{}.mxd".format(mxd_name))
        # mxd2 = arcpy.mapping.MapDocument(r"C:\Users\QC7\Documents\ArcGIS\arcpyProjects\data\{}.mxd".format(mxd_name))
        lyr_list = arcpy.mapping.ListLayers(mxd)
        layer = lyr_list[0]

        # 引用样式
        arcpy.ApplySymbologyFromLayer_management(layer, my_lyr)
        legend = arcpy.mapping.ListLayoutElements(mxd, "LEGEND_ELEMENT")[0]
        legend.title = png_name + str1

        arcpy.mapping.ExportToPNG(mxd, png_path + "\\" + "{0}.png".format(png_name), resolution=300)
        del mxd
