# -*- coding:utf-8 -*-

import arcpy
import os
import sys

reload(sys)

# 添加中文支持
sys.setdefaultencoding('utf8')
arcpy.env.overwriteOutput = True
# arcpy.env.workspace = r"C:\Users\QC7\Documents\ArcGIS\arcpyProjects\wz_test1.gdb"

str1 = ' 人/平方千米'


def get_choropleth_map(shp_path, data_path, my_lyr_path, mxd_path, png_path, join_field1, join_field2, cal_field1, cal_field2, res_field):
    files = os.listdir(data_path.encode("gbk").decode("utf-8"))
    for i in files:
        file_path = data_path + '\\' + i
        filename = os.path.basename(i)
        png_name = os.path.basename(i).split('.')[0]
        my_lyr = arcpy.mapping.Layer(my_lyr_path)
        mxd = arcpy.mapping.MapDocument(mxd_path)
        layer = arcpy.mapping.ListLayers(mxd)[0]

        fieldnames = [f.name for f in arcpy.ListFields(shp_path)]
        if 'res' not in fieldnames:
            arcpy.AddField_management(shp_path, 'res', 'DOUBLE', 18, 11)
        if 'cov2' not in fieldnames:
            arcpy.AddField_management(shp_path, 'cov2', 'DOUBLE', 18, 11)
        # df = arcpy.mapping.ListDataFrames(mxd)[0]
        join_table = file_path
        arcpy.AddJoin_management(layer, join_field1, join_table, join_field2)
        expression1 = "cal_cov2(!{0}.{1}!)".format(filename, cal_field2)
        code_block = """def cal_cov2(ctb):
            if ctb:
                return ctb
            else:
                return 0
        """
        expression2 = '!{0}.{1}!/!{2}.{3}!'.format(layer, 'cov2', layer, cal_field1)
        arcpy.CalculateField_management(layer, 'cov2', expression1, "PYTHON_9.3", code_block)
        arcpy.CalculateField_management(layer, res_field, expression2, "PYTHON_9.3")
        arcpy.RemoveJoin_management(layer)
        arcpy.ApplySymbologyFromLayer_management(layer, my_lyr)

        legend = arcpy.mapping.ListLayoutElements(mxd, "LEGEND_ELEMENT")[0]
        legend.title = png_name + str1
        arcpy.mapping.ExportToPNG(mxd, png_path + "\\" + "{0}.png".format(png_name), resolution=300)
        del mxd
