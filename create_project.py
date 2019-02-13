import os
from shutil import copyfile

project_name = 'test'
dir_base = 'c:/projects/Occasional'
dir_project = os.path.join(dir_base, project_name)

bool_ci5plus= True
bool_norpred = False

if not os.path.exists(dir_project):

    os.makedirs(dir_project)
    os.makedirs(os.path.join(dir_project, '_figs'))
    os.makedirs(os.path.join(dir_project, '_data'))
    os.makedirs(os.path.join(dir_project, '_dict'))
    os.makedirs(os.path.join(dir_project, '_table'))

    do_file = open(os.path.join(dir_project,'main.do'),"w+")
    do_file.write('set trace off\r')
    do_file.write('set more off\r')
    do_file.write('clear all\r\n')

    do_file.write('global dir_main ' + '"' + dir_project.replace('/', '\\') + '"' + '\r')
    do_file.write('global dir_figs  "${dir_main}\\_figs"\r')
    do_file.write('global dir_dict  "${dir_main}\\_dict"\r')
    do_file.write('global dir_dta "${dir_main}\\_data"\r\n')

    do_file.write('global dir_DATA "C:\\data"\r')
    do_file.write('global dir_SHAPE "${dir_DATA}\\_shape"\r')
    do_file.write('global dir_UNcode "${dir_DATA}\\UNcode"\r')
    do_file.write('global dir_UNDPpop "${dir_DATA}\\UNDPpop"\r')
    do_file.write('global dir_CI5plus "${dir_DATA}\\CI5plus"\r')
    do_file.write('global dir_CI5XI "${dir_DATA}\\CI5XI"\r')
    do_file.write('global dir_GLOBO2018 "${dir_DATA}\\Globocan2018"\r')
    do_file.write('global dir_GHE "${dir_DATA}\\GHE_mortality"\r')
    do_file.write('global dir_WHO_mortality  "${dir_DATA}\\WHO_mortality"\r\n')

    do_file.write('global dir_inkbash  "C:\\Projects\\inkbash"\r')
    do_file.write('global dir_fix_label  "${dir_inkbash}\\fix_label"\r\n')

    do_file.write('global dir_maps_data "C:\\Projects\\Standard_maps\\_data"\r\n')

    do_file.write('*begin store local color \r\n')

    do_file.write('local HDI_violet "182 44 161"\r\n')

    do_file.write('local HDI_red "215 25 28"\r')
    do_file.write('local HDI_orange "230 97 1"\r')
    do_file.write('local HDI_midblue "171 217 233"\r')
    do_file.write('local HDI_blue "44 123 182"\r\n')

    do_file.write('local HDI_midblue_focus "104 195 228"\r\n')

    do_file.write('local col_europe  "55 126 184"\r')
    do_file.write('local col_NAmerica  "152 78 163"\r')
    do_file.write('local col_SAmerica "205 52 90" \r')
    do_file.write('local col_Oceania  "246 125 56"\r')
    do_file.write('local col_Asia "48 191 48"\r')
    do_file.write('local col_Africa "242 240 52"\r\n')

    do_file.write('local color_cat1 "30 144 255"\r')
    do_file.write('local color_cat2 "52 167 110"\r')
    do_file.write('local color_cat3 "220 19 65"\r')
    do_file.write('local color_cat4 "255 117 0"\r\n')

    do_file.write('// prepare color \r')
    do_file.write('insheet using "${dir_DATA}\_dict\color_trend.csv", comma clear name\r\n')

    do_file.write('forvalues i =1/ 27 {\r')
    do_file.write(" local color`i' = color[`i']\r")
    do_file.write(' //di "`color`i"\r')
    do_file.write(' }\r\n')

    do_file.write('*end \r\n')

    do_file.close()


    r_file = open(os.path.join(dir_project,'main.r'),"w+")
    r_file.write('setwd(' + '"' + dir_project.replace('\\', '/') + '")\r\n')

    r_file.write('library(ggplot2)\r')
    r_file.write('library(data.table)\r')
    r_file.write('library(Rcan)\r\n')
    r_file.close()

    if (bool_ci5plus):
        copyfile('./CI5plus_registry_selection.csv', os.path.join(dir_project, '_dict', './CI5plus_registry_selection.csv'))
