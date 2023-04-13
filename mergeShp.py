# -*- coding:utf-8 -*-
# 合并多个shp

import pandas as pd
import arcpy
import os
import sys

arcpy.env.overwriteOutput = True
reload(sys)
sys.setdefaultencoding('utf8')

shps = []
path = r'E:\Desktop\shp\沈阳市'
for i in os.listdir(unicode(path, 'utf-8')):
    path_shp = r'E:\Desktop\shp\沈阳市\{}'.format(i)
    for j in os.listdir(unicode(path_shp, 'utf-8')):
        if j.endswith(".shp"):
            j_path = r'E:\Desktop\shp\沈阳市\{}\{}'.format(i,j)
            shps.append(os.path.join(path_shp, j_path))
output = r'E:\Desktop\shp\test_merge'
arcpy.Merge_management(shps, output)