# -*- coding:utf-8 -*-
# 批量添加字段

import pandas as pd
import arcpy
import os
import sys

arcpy.env.overwriteOutput = True
reload(sys)
sys.setdefaultencoding('utf8')

path = r'E:\Desktop\shp\沈阳市'
for i in os.listdir(unicode(path, 'utf-8')):
    path_shp = r'E:\Desktop\shp\沈阳市\{}'.format(i)
    for j in os.listdir(unicode(path_shp, 'utf-8')):
        if j.endswith(".shp"):
            shp = r'E:\Desktop\shp\沈阳市\{}\{}'.format(i,j)
            xzq = j.split('.')[0].split('_')[0]

            field_name1 = 'xzq'
            field_name2 = 'city'
            fieldnames = [f.name for f in arcpy.ListFields(shp)]

            if field_name1 not in fieldnames:
                arcpy.AddField_management(shp, field_name1, 'TEXT', field_length=50)

            if field_name2 not in fieldnames:
                arcpy.AddField_management(shp, field_name2, 'TEXT', field_length=50)

            expression1 = "addAttr(\"{}\")".format(xzq)
            expression2 = "addAttr(\"{}\")".format("沈阳市")
            code_block = """def addAttr(attrName):
                    return attrName
            """
            arcpy.CalculateField_management(shp, field_name1, expression1, "PYTHON_9.3", code_block)
            arcpy.CalculateField_management(shp, field_name2, expression2, "PYTHON_9.3", code_block)
