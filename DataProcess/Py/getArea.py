# -*- coding:utf-8 -*-
# 投影坐标选择
# 6位带CM 8位带Zone; 3 Degree 为3度带，否则为6度带
# 3度带为例, N = 经度/3 有余数则加1; L = 3*N

import arcpy
import sys

arcpy.env.overwriteOutput = True
reload(sys)
sys.setdefaultencoding('utf8')


def get_area(shp):
    fieldnames = [f.name for f in arcpy.ListFields(shp)]
    if 'Area' not in fieldnames:
        arcpy.AddField_management(shp, 'Area', 'DOUBLE', 18, 11)
    arcpy.CalculateField_management(shp, 'Area', '!shape.area@squarekilometers!', "PYTHON_9.3")

