# -*- coding:utf-8 -*-
# PYTHON_9.3 —表达式将使用标准 Python 格式编写。地理处理器方法和属性的使用与创建 9.3 版地理处理器相同。

import arcpy
import sys

arcpy.env.overwriteOutput = True
reload(sys)
sys.setdefaultencoding('utf8')


def project_to_wgs84(shp_path, shp_out_path):
    out_cs = arcpy.SpatialReference('WGS 1984')
    arcpy.Project_management(shp_path, shp_out_path, out_cs)


def wgs84_to_project(shp_path, shp_out_path, lon):
    degree_type = 3
    precision = 8
    div = divmod(lon, degree_type)[0]
    mod = divmod(lon, degree_type)[1]
    if mod == 0:
        n = div
    else:
        n = div + 1
    l_number = 3*n
    if precision == 8:
        out_cs_name = 'CGCS2000 3 Degree GK Zone {0}'.format(n)
    else:
        out_cs_name = 'CGCS2000 3 Degree GK CM {0}E'.format(l_number)

    out_cs = arcpy.SpatialReference(out_cs_name)
    arcpy.Project_management(shp_path, shp_out_path, out_cs)