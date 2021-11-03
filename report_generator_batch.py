# -*- coding: utf-8 -*-

####################################################
#This script tool need the following dictionaries: #
# [*] Need dictionaries/dicts_analysis_layers.py   #
# [*] Need dictionaries/dict_alias_names.py        #
####################################################

# Required libraries.
import arcpy
import os
from alias_names_min import *
from analysis_layers_min import *

# Define a class Categoria wich is previously defined in dictionaries/dict_analysis_layers.py.
class Categoria(object):
	# Need a predefined dictionary (all dictionaries for this project are in dictionaries/dicts_analysis_layers.py).
	def __init__(self, category_name, category_dictionary):
		self.category_name = category_name
		self.category_dictionary = category_dictionary

	def report_writer(self):
		f.write('\n\n{}\n'.format(self.category_name))
		f.write('CAMADA|CLASSE REGISTRADA|DESCRIÇÃO|DETALHAMENTO|ÁREA (ha) |% da área\n')
		for fc in fc_list:
			if fc in self.category_dictionary.keys():
				fc_description = arcpy.Describe(fc)
				fc_cursor = arcpy.SearchCursor(fc)
				for row in fc_cursor:
					f.write(alias_names[fc] + '|')
					exec(self.category_dictionary[fc])
					f.write('\n')
				if int(arcpy.GetCount_management(fc).getOutput(0)) == 0:
					f.write(alias_names[fc] + '|Não foram encontrados registros para esta camada.|—|—|—\n')

	def report_writer_apcb(self):
		f.write('\n\n{}\n'.format(self.category_name))
		f.write('NOME DA ÁREA PRIORITÁRIA|PROTEÇÃO AOS RECURSOS HÍDRICOS|CRIAÇÃO DE UNIDADES DE CONSERVAÇÃO|RESTAURAÇÃO DE CORREDORES ECOLÓGICOS|COTA DE RESERVA AMBIENTAL|FOMENTO AO USO SUSTENTÁVEL|FORTALECIMENTO DE UNIDADES DE CONSERVAÇÃO|IMPORTÂNCIA BIOLÓGICA|PRIORIDADE|ÁREA (ha)\n')
		for fc in fc_list:
			if fc in self.category_dictionary.keys():
				fc_description = arcpy.Describe(fc)
				fc_cursor = arcpy.SearchCursor(fc)
				for row in fc_cursor:
					exec(self.category_dictionary[fc])
					f.write('\n')
				if int(arcpy.GetCount_management(fc).getOutput(0)) == 0:
					f.write(alias_names[fc] + '|Não foram encontrados registros para esta camada.|—|—|—\n')


arcpy.env.workspace = u'S:\\04_geosema\\03_projetos\\map\\map_simulator\\_out_clips\\'
ws = arcpy.ListWorkspaces()

for w in ws:
	
	arcpy.env.workspace = w
	project_name = os.path.basename(arcpy.env.workspace).replace('.gdb', '')

	os.chdir('S:\\04_geosema\\03_projetos\\map\\map_simulator\\_reports\\')

	fc_list = arcpy.ListFeatureClasses()
	
	f = open(project_name + '_report.csv', 'w+')

	areas_prioritarias = Categoria('AREAS PRIORITARIAS', areas_prioritarias_dict)
	areas_prioritarias.report_writer_apcb()
	
	dados_ambientais = Categoria('DADOS AMBIENTAIS', dados_ambientais_dict)
	dados_ambientais.report_writer()

	dados_socio = Categoria('DADOS SOCIO', dados_socio_dict)
	dados_socio.report_writer()

	meio_fisico = Categoria('MEIO FÍSICO', meio_fisico_dict)
	meio_fisico.report_writer()

	restricoes_legais = Categoria('RESTRIÇÕES LEGAIS', restricoes_legais_dict)
	restricoes_legais.report_writer()

	infraestrutura_hidrica = Categoria('INFRAESTRUTURA HÍDRICA', infraestrutura_hidrica_dict)
	infraestrutura_hidrica.report_writer()

	f.close()