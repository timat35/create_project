import os
from shutil import copyfile


#sublime regex

#^(.*+)
#r_file.write\('\1\\r'\)




#\\r'\)\n\n
#\\r\\n'\)\n\n



project_name = 'LatinAmerica'
dir_base = 'C:/Projects/globocan2018_graph/region'
dir_project = os.path.join(dir_base, project_name)

bool_ci5XI= True
bool_ci5plus= True
bool_norpred = False

bool_map_general = False
bool_map_detailed = True

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
    do_file.write('insheet using "${dir_DATA}\\_dict\\color_trend.csv", comma clear name\r\n')

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

    if (bool_map_general):

        r_file.write('source("C:/Projects/Standard_maps/general_WHO_map.r")\r')

        r_file.write('colors_hdi <- c("#D7191C","#E66101","#ABD9E9","#2C7BB6")\r')
        r_file.write('colors_incidence_5 <-  c( "#eff3ff","#b5cae6","#7ba2cd", "#4179b4","#08519c")\r')
        r_file.write('colors_mortality_5 <-  c( "#fee5d9","#fcae91", "#fb6a4a","#de2d26", "#a50f15")\r')

        r_file.write('color_graph <- colors_incidence_5\r\n')

        r_file.write('colorBlues<- colorRampPalette(c("#eff3ff","#08519c"))\r')
        r_file.write('colorRed<- colorRampPalette(c("#fee5d9","#a50f15"))\r')        

    if (bool_map_detailed):

        r_file.write('colors_hdi <- c("#D7191C","#E66101","#ABD9E9","#2C7BB6")\r')
        r_file.write('colors_incidence_5 <-  c( "#eff3ff","#b5cae6","#7ba2cd", "#4179b4","#08519c")\r')
        r_file.write('colors_mortality_5 <-  c( "#fee5d9","#fcae91", "#fb6a4a","#de2d26", "#a50f15")\r\n')

        r_file.write('color_graph <- colors_incidence_5\r\n')

        r_file.write('colorBlues<- colorRampPalette(c("#eff3ff","#08519c"))\r')
        r_file.write('colorRed<- colorRampPalette(c("#fee5d9","#a50f15"))\r\n')

        r_file.write('#http://projectionwizard.org/\r')
        r_file.write('#EURO\r')
        r_file.write('temp_proj <- "+proj=aea +lat_1=41.4 +lat_2=65.1 +lon_0=32.3"\r\n')

        r_file.write('source("C:/Projects/Standard_maps/detailled_WHO_map.r")\r\n')

        r_file.write('#specific to region\r\n')

        r_file.write('  df_poly_layout\r')
        r_file.write('  poly_list <- c(9)\r\n')

        r_file.write('  df_line_layout\r')
        r_file.write('  line_list <- NULL\r\n')

        r_file.write('  # prepare selected area shape files ------------\r\n')

        r_file.write('  dt_selection <- as.data.table(read.csv("C:/Data/country_selection/latinAmericaCaribbean.csv"))\r')
        r_file.write('  dt_selection <- dt_selection[selection == 1 | outmap ==1,]\r\n')

        r_file.write('  dt_select_id <- merge(dt_selection, dt_shape, by=c("country_code"),all.x=TRUE,suffixes = c("",".y"))\r\n')

        r_file.write('  #check no missing id\r')
        r_file.write('  nrow(dt_select_id[is.null(id),])\r')
        r_file.write('  dt_select_id[, country_label.y := NULL]\r\n')

        r_file.write('#---- example merge with dataset globocan 2018----# \r\n')

        r_file.write('  dt_data <- as.data.table(read.csv("C:/Data/Globocan2018/Globocan_asr_cases_cumrisk.csv"))\r')
        r_file.write('  dt_data <- dt_data[country_code <900,]\r\n')

        r_file.write('  dt_data[, missing:=TRUE]\r')
        r_file.write('  dt_data <- merge(dt_data, dt_select_id, by=c("country_code"),all.y=TRUE,suffixes = c("",".y"))\r\n')

        r_file.write('  #see missing data\r')
        r_file.write('  unique(dt_data[is.na(missing),]$country_label.y)\r\n')

        r_file.write('  #manage missing data\r')
        r_file.write('  dt_map_missing <- dt_data[is.na(missing) & outmap!= 1,c("country_label.y", "id")]\r')
        r_file.write('  dt_map_missing <- merge(df_map, dt_map_missing, by = c("id"), all.y=TRUE, sort=F )\r')
        r_file.write('  dt_map_missing <- dt_map_missing[order(dt_map_missing$int_map_index),]\r\n')

        r_file.write('  #manage outmap \r')
        r_file.write('  dt_map_out <-  unique(dt_data[outmap ==1,c("country_label", "id")])\r')
        r_file.write('  dt_map_out <- merge(df_map, dt_map_out, by = c("id"), all.y=TRUE, sort=F )\r')
        r_file.write('  dt_map_out <- dt_map_out[order(dt_map_out$int_map_index),]\r\n')

        r_file.write('  #keep only data\r')
        r_file.write('  dt_data <- dt_data[!is.na(missing) & outmap == 0,]\r\n')
        r_file.write('  dt_data[, country_label.y := NULL]\r\n')


        r_file.write('#------ First cancer map detailled for the example------------ #\r\n')

        r_file.write('  dt_data[,c("asr", "cumrisk") := NULL]\r')
        r_file.write('  dt_data <- dt_data[!cancer_code %in% c(17,37,38,39,40),]\r\n')


        r_file.write('  dt_data<- Rcan:::core.csu_dt_rank(dt_data, \r')
        r_file.write('      var_value = "cases",\r')
        r_file.write('      var_rank = "cancer_label",\r')
        r_file.write('      group_by = c("type","sex","country_code"),\r')
        r_file.write('      number = 1)\r\n')

        r_file.write('  dt_data <- dt_data[type == 1 & sex == 2,]\r\n')

        r_file.write('  dt_data$cancer_label <- factor(dt_data$cancer_label)\r')
        r_file.write('  temp<- table(dt_data$cancer_label) \r')
        r_file.write('  temp <- sort(temp, decreasing = TRUE)\r')
        r_file.write('  dt_data$cancer_label <- factor(dt_data$cancer_label,levels = names(temp)) \r')
        r_file.write('  nrow(temp)\r')
        r_file.write('  names(temp)\r\n')

        r_file.write('  labels_leg <- c(paste0(names(temp)[1]," (",temp[[1]],")"))\r\n')

        r_file.write('  for (i in 2:(nrow(temp))) {\r')
        r_file.write('    labels_leg <- c(labels_leg, paste0(names(temp)[i]," (",temp[[i]],")"))\r')
        r_file.write('  }\r\n')

        r_file.write('  # merge name and color\r')
        r_file.write('  df_color <- read.csv("C:/Data/_dict/cancer_color_2018.csv", sep=",")\r')
        r_file.write('  df_color <- subset(df_color, select = c(cancer_label, Color.Hex))\r')
        r_file.write('  df_name <- data.frame(names(temp))\r')
        r_file.write('  colnames(df_name)[1] <- "cancer_label"\r')
        r_file.write('  df_color_map <- merge(df_name, df_color, by = c("cancer_label"), all.x=TRUE, sort=F )\r')
        r_file.write('  df_color_map[] <- lapply(df_color_map, as.character)\r')
        r_file.write('  color_graph <- c(df_color_map$Color.Hex)\r\n')

        r_file.write('  # merge with shape file\r')
        r_file.write('  df_data_map <- merge(df_map, dt_data, by = c("id"), all.y=TRUE, sort=F )\r')
        r_file.write('  df_data_map <- df_data_map[order(df_data_map$int_map_index),]\r\n')

        r_file.write('  df_data_map$fill <- df_data_map$cancer_label\r\n')

        r_file.write('  plot <- plot_det_map(df_data_map,legend_title = "Mortality, females", legend_reverse=FALSE) \r')
        r_file.write('  #plot\r\n')

        r_file.write('  file_label <- paste0("_figs/map_mortality_first_EURO_female")\r')
        r_file.write('  file_svg <- paste0(file_label, ".svg")\r')
        r_file.write('  file_pdf <- paste0(file_label, ".pdf")\r')
        r_file.write('  map_source_prod <- \' "Globocan 2018" "CSU"\'\r\n')

        r_file.write('  svg(file_svg,width = 40, height = 40, pointsize = 12)\r')
        r_file.write('  print(plot)\r')
        r_file.write('  dev.off()\r\n')

        r_file.write('  system(paste0(\'python "c:/Projects/inkbash/st_maps/st_map_det.py"\' , file_svg, map_source_prod),\r')
        r_file.write('         wait=FALSE, intern = TRUE)\r\n')



    r_file.close()
    
    if (bool_ci5XI):
        copyfile('./CI5XI_registry_selection.csv', os.path.join(dir_project, '_dict', './CI5XI_registry_selection.csv'))

    if (bool_ci5plus):
        copyfile('./CI5plus_registry_selection.csv', os.path.join(dir_project, '_dict', './CI5plus_registry_selection.csv'))
