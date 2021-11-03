# -*- coding: utf-8 -*-
# Simulate some analysis realized from MAP/Geobahia
# This version is adapted to use geodatabase
# Need to project all input files into Albers Equal Area


# Import libraries
import glob
import arcpy
import os

# Defining variables to work directories and geodatabases
areas_of_interest_dir = u"S:\\04_geosema\\03_projetos\\map\\map_simulator\\_in_areas\\"
out_dir = u"S:\\04_geosema\\03_projetos\\map\\map_simulator\\_out_clips\\"
base_maps_gdb = u"S:\\04_geosema\\03_projetos\\map\\map_simulator\\_databases\\map_geodatabase_analysis.gdb"


# Defining feature classes of areas of interest
areas_of_interest = glob.glob(areas_of_interest_dir + '*.shp')

# Generate clips
for interest_area in areas_of_interest:
	if not os.path.exists(out_dir + os.path.basename(interest_area).replace('.shp','')):
		arcpy.CreateFileGDB_management(out_dir, os.path.basename(interest_area).replace('.shp','.gdb'))

	arcpy.env.workspace = base_maps_gdb
	base_maps_list = arcpy.ListFeatureClasses()
	for base_map in base_maps_list:
		if not base_map == 'RPPN_Federais_ICMBIO_2014':
			arcpy.Clip_analysis(base_map, interest_area, out_dir + os.path.basename(interest_area).replace('.shp','.gdb') + '\\' + base_map)