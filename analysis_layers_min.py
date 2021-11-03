# -*- coding: utf-8 -*-
# dictionaries of layers and respective properties based on classes

areas_prioritarias_dict = {
'Apcb_sema_2015' : "f.write('{0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9}'.format(row.getValue('apcb_nome').encode('utf-8'), row.getValue('Prot_RH').encode('utf-8'), row.getValue('CriaUC').encode('utf-8'), row.getValue('RestCorr').encode('utf-8'), row.getValue('CRA').encode('utf-8'), row.getValue('FomentoUS').encode('utf-8'), row.getValue('FortalUC').encode('utf-8'), row.getValue('ImpBiol').encode('utf-8'), row.getValue('Prioridade').encode('utf-8'), str(row.getValue('Shape_Area')/10000).replace('.',',')))",	
}

# print format: CLASSE REGISTRADA   |DESCRICAO   | DETALHAMENTO      |AREA |

dados_ambientais_dict = {
'Indice_frag_sema_2015' : "f.write(row.getValue('Classe').encode('utf-8') + '|' + '—' + '|' + '—' + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Relev_amb_sema_2015' : "f.write(row.getValue('Classe_ra').encode('utf-8')+ '|' + '—' + '|' + '—' + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Uni_paisagem_zee_2013' : "f.write('—' + '|' + row.getValue('UP_NOME').encode('utf-8') + '|' + row.getValue('UP_DESC').encode('utf-8') + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Veg_100k_seagri_1998' : "f.write(row.getValue('NM_CLASSE').encode('utf-8')+ '|' + '—' + '|' + '—' + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Vul_amb_sema_2015' : "f.write(row.getValue('Classe_va').encode('utf-8')+ '|' + '—' + '|' + '—' + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Vuln_Risco_Nat_Aguas_Subterraneas_ZEE_2013' : "f.write(row.getValue('Vuln_Nat').encode('utf-8') + '|' + '—' + '|' + '—' + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Vulnerabilidade_Hidrica_ZEE_2013' : "f.write(row.getValue('CLASSIFICA').encode('utf-8')+ '|' + '—' + '|' + '—' + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Vulnerabilidade_Erosao_ZEE_2013' : "f.write(row.getValue('Class_VUL2').encode('utf-8') + '|' + '—' + '|' + '—' + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
}

dados_socio_dict = {
'Zee_sema_2013' : "f.write(row.getValue('Zona_Nome').encode('utf-8')+ '|' + '---' + '|' + '---' + '|' + str(row.getValue('Shape_Area')).replace('.',','))",
'Assent_incra_2011' : "f.write('—' + '|' + row.getValue('NOMEPROJ3').encode('utf-8') + '|' + row.getValue('MUNICIPI9').encode('utf-8') + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Sitios_barqueol_2012' : "f.write(row.getValue('Classifica').encode('utf-8')+ '|' + row.getValue('Nome_do_S').encode('utf-8')+ '|' + row.getValue('Município').encode('utf-8') + '|' + '—')",
'Densidfundpasto_cda_2014' : "f.write('—'+ '|' + str(row.getValue('Quantidade')).replace('.',',')+ '|' + row.getValue('MUNICIPIO').encode('utf-8') + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Indige_ba_mma_2010' : "f.write(row.getValue('GRUPOS').encode('utf-8') + '|' + row.getValue('NOME_TI').encode('utf-8') + '|' + row.getValue('MUNICíPIO').encode('utf-8')+ '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Patritomb_iphan_2014' : "f.write('—' + '|' + row.getValue('Patrimôni').encode('utf-8') + '|' + row.getValue('MUNICIPIO').encode('utf-8') + '|' + '—')",
'Quilomb_incra_2010' : "f.write('—' + '|' + row.getValue('Territóri').encode('utf-8')+ '|' + row.getValue('Município').encode('utf-8') + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Relev_social_sema_2015' : "f.write(row.getValue('NOTA_rsoc').encode('utf-8') + '|' + '—' + '|' + '—' + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Vul_social_sema_2015' : "f.write(row.getValue('Classe_vs').encode('utf-8')+ '|' + '—' + '|' + '—' + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
}

meio_fisico_dict = {
'Geomorfologia_zee_2012' : "f.write(row.getValue('nome_desc').encode('utf-8') + '|' + '—' + '|' + '—' + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Unidades_Territoriais_Basicas_ZEE_2013' : "f.write('—' + '|' + row.getValue('UTB_NOME').encode('utf-8') + '|' + row.getValue('DESCRIÇAO').encode('utf-8') + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
}

restricoes_legais_dict = {
'Cavernas_CECAV_2014' : "f.write('—' + '|' + row.getValue('NOME').encode('utf-8') + '|' + row.getValue('MUNICíPIO').encode('utf-8') + '|' + '—')",
'Relev_amb_sema_2015' : "f.write(row.getValue('Classe_ra').encode('utf-8')+ '|' + '—' + '|' + '—' + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Relev_social_sema_2015' : "f.write(row.getValue('NOTA_rsoc').encode('utf-8') + '|' + '—' + '|' + '—' + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'RPPN_Federais_ICMBIO_2014' : "f.write('Uso Sustentável' + '|' + row.getValue('nome').encode('utf-8') + '|' + row.getValue('municipio').encode('utf-8') + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Uc_icmbio_2011' : "f.write(row.getValue('Sigla_Gr').encode('utf-8') + '|' + row.getValue('Nom_Dec').encode('utf-8')+ '|' + row.getValue('municipios').encode('utf-8') + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Uc_inema_2014' : "f.write(row.getValue('GRUPO').encode('utf-8') + '|' + row.getValue('NOME_UC').encode('utf-8')+ '|' + row.getValue('MUNICIPIOS').encode('utf-8') + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Zauc_3km_fed_sema_2014' : "f.write(row.getValue('Sigla_Gr').encode('utf-8')+ '|' + row.getValue('Nom_Dec').encode('utf-8') + '|' + row.getValue('municipios').encode('utf-8')+ '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Zauc_3km_inema_2010' : "f.write(row.getValue('Grupo').encode('utf-8') + '|' + row.getValue('Nome_UC').encode('utf-8') + '|' + row.getValue('Municipios').encode('utf-8')+ '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Zauc_inema_2014' : "f.write(row.getValue('Grupo').encode('utf-8') + '|' + row.getValue('Nome_UC').encode('utf-8') + '|' + row.getValue('Municipios').encode('utf-8')+ '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
}

infraestrutura_hidrica_dict = {
'Barragens_inema_2010' : "f.write(row.getValue('ACUDE_BARR').encode('utf-8') + '|' + '---' + '|' + '---' + '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
'Pivos_ba_2014': "f.write('---' + '|' + '---' + '|' + '---'+ '|' + str(row.getValue('Shape_Area')/10000).replace('.',','))",
}