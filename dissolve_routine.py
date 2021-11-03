# need import dict_dissolve_layers_min.py

import arcpy
import os

arcpy.env.workspace = 'gdb_dir'
out_gdb = 'out_gdb_dir\\'

fc_list = arcpy.ListFeatureClasses()

for fc in fc_list:
	# 1) export points to new gaodatabase
	fc_description = arcpy.Describe(fc)
	if fc_description.shapeType == 'Point':
		arcpy.FeatureClassToGeodatabase_conversion(fc,out_gdb)
	# 2) Dissolve
	if fc in dissolve_dict:
		arcpy.Dissolve_management(fc, out_gdb + fc, dissolve_dict[fc])