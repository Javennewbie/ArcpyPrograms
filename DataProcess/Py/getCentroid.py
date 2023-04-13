# -*- coding:utf-8 -*-
# PYTHON_9.3 —表达式将使用标准 Python 格式编写。地理处理器方法和属性的使用与创建 9.3 版地理处理器相同。


import pandas as pd
import arcpy
import os
import sys

arcpy.env.overwriteOutput = True
reload(sys)
sys.setdefaultencoding('utf8')


def get_centroid(shp, primary_key, out_location, out_table_name, label='en'):
    if label == 'zh':
        out_location = out_location.encode("gbk")

    out_table = out_table_name + '.csv'
    field_precision = 18  # 字段位数，大于6为双精度
    field_scale = 11  # 小数位数
    field_name1 = 'centroidX'
    field_name2 = 'centroidY'
    fieldnames = [f.name for f in arcpy.ListFields(shp)]

    if field_name1 not in fieldnames and field_name2 not in fieldnames:
        arcpy.AddField_management(shp, field_name1, 'DOUBLE', field_precision, field_scale)
        arcpy.AddField_management(shp, field_name2, 'DOUBLE', field_precision, field_scale)

    arcpy.CalculateField_management(shp, field_name1, "!SHAPE.CENTROID.X!", "PYTHON_9.3")
    arcpy.CalculateField_management(shp, field_name2, "!SHAPE.CENTROID.Y!", "PYTHON_9.3")
    fm = arcpy.FieldMap()
    fm1 = arcpy.FieldMap()
    fm2 = arcpy.FieldMap()
    fm.addInputField(shp, primary_key)
    fm1.addInputField(shp, field_name1)
    fm2.addInputField(shp, field_name2)
    fms = arcpy.FieldMappings()
    fms.addFieldMap(fm)
    fms.addFieldMap(fm1)
    fms.addFieldMap(fm2)
    arcpy.TableToTable_conversion(shp, out_location, out_table, field_mapping=fms)
    os.remove(out_location + '\\' + 'schema.ini')
    os.remove(out_location + '\\' + '{0}.txt.xml'.format(out_table_name))
    # # 筛选所需字段，转换编码
    centroid_data = pd.read_csv(out_location + '\\' + out_table)
    centroid_data = centroid_data[[primary_key, field_name1, field_name2]]
    centroid_data.to_csv(out_location + '\\' + out_table, index=False, encoding='gbk')