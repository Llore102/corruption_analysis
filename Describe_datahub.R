## install.packages("readr")

## Librerías a usar
  library(readr)
  library(readxl)
  
## Ruta de trabajo
  ruta <- "C:/Users/llore/R/Proyectos/Sunat/"
  ruta_out <- "C:/Users/llore/R/Proyectos/Sunat"

  data_cons <- read_excel(paste0(ruta, 'Adjudicaciones.xlsx'))

  # Seleccionamos solo variables numéricas
    data_numeric <- data_cons[, sapply(data_cons, is.numeric)]
  
  # Realizamos el describe
    description <- psych::describe(data_numeric)
  
  # Calculamos los percentiles y el IQR para cada variable
    percentiles_iqr <- lapply(data_numeric, function(x) {
      quantiles <- quantile(x, c(0.25, 0.75), na.rm = TRUE)
      iqr_value <- IQR(x, na.rm = TRUE)
      c(quantiles[1], quantiles[2], IQR = iqr_value)
    })
  
  # Convertimos la lista de resultados a un dataframe
    percentiles_iqr_df <- as.data.frame(do.call(rbind, percentiles_iqr))
  
  # Juntamos los describe con los percentiles en un nuevo dataframe
    descriptivos <- cbind(description, percentiles_iqr_df)
  
  # Apuntamos a la ruta de salida
    output_file <- file.path(ruta_out, 'Adjudicaciones_describe.csv')
  
  # Exportamos el csv 
    write.csv(descriptivos, file = output_file)
  
  # Mensaje del save exitoso
    cat("La descripción se ha guardado en", output_file, "\n")

    
##### ----- Postores -------- #######
    
    data_cons <- read_excel(paste0(ruta, 'Postor.xlsx'))
    
    # Seleccionamos solo variables numéricas
    data_numeric <- data_cons[, sapply(data_cons, is.numeric)]
    
    # Realizamos el describe
    description <- psych::describe(data_numeric)
    
    # Calculamos los percentiles y el IQR para cada variable
    percentiles_iqr <- lapply(data_numeric, function(x) {
      quantiles <- quantile(x, c(0.25, 0.75), na.rm = TRUE)
      iqr_value <- IQR(x, na.rm = TRUE)
      c(quantiles[1], quantiles[2], IQR = iqr_value)
    })
    
    # Convertimos la lista de resultados a un dataframe
    percentiles_iqr_df <- as.data.frame(do.call(rbind, percentiles_iqr))
    
    # Juntamos los describe con los percentiles en un nuevo dataframe
    descriptivos <- cbind(description, percentiles_iqr_df)
    
    # Apuntamos a la ruta de salida
    output_file <- file.path(ruta_out, 'Postor_describe.csv')
    
    # Exportamos el csv 
    write.csv(descriptivos, file = output_file)
    
    # Mensaje del save exitoso
    cat("La descripción se ha guardado en", output_file, "\n")
    

##### ----- CONTRATO -------- #######
    
    data_cons <- read_excel(paste0(ruta, 'Contrato.xlsx'))
    
    # Seleccionamos solo variables numéricas
    data_numeric <- data_cons[, sapply(data_cons, is.numeric)]
    
    # Realizamos el describe
    description <- psych::describe(data_numeric)
    
    # Calculamos los percentiles y el IQR para cada variable
    percentiles_iqr <- lapply(data_numeric, function(x) {
      quantiles <- quantile(x, c(0.25, 0.75), na.rm = TRUE)
      iqr_value <- IQR(x, na.rm = TRUE)
      c(quantiles[1], quantiles[2], IQR = iqr_value)
    })
    
    # Convertimos la lista de resultados a un dataframe
    percentiles_iqr_df <- as.data.frame(do.call(rbind, percentiles_iqr))
    
    # Juntamos los describe con los percentiles en un nuevo dataframe
    descriptivos <- cbind(description, percentiles_iqr_df)
    
    # Apuntamos a la ruta de salida
    output_file <- file.path(ruta_out, 'Contrato_describe.csv')
    
    # Exportamos el csv 
    write.csv(descriptivos, file = output_file)
    
    # Mensaje del save exitoso
    cat("La descripción se ha guardado en", output_file, "\n")
    

##### ----- Convocatorias -------- #######
    
    data_cons <- read_excel(paste0(ruta, 'Convocatorias.xlsx'))
    
    # Seleccionamos solo variables numéricas
    data_numeric <- data_cons[, sapply(data_cons, is.numeric)]
    
    # Realizamos el describe
    description <- psych::describe(data_numeric)
    
    # Calculamos los percentiles y el IQR para cada variable
    percentiles_iqr <- lapply(data_numeric, function(x) {
      quantiles <- quantile(x, c(0.25, 0.75), na.rm = TRUE)
      iqr_value <- IQR(x, na.rm = TRUE)
      c(quantiles[1], quantiles[2], IQR = iqr_value)
    })
    
    # Convertimos la lista de resultados a un dataframe
    percentiles_iqr_df <- as.data.frame(do.call(rbind, percentiles_iqr))
    
    # Juntamos los describe con los percentiles en un nuevo dataframe
    descriptivos <- cbind(description, percentiles_iqr_df)
    
    # Apuntamos a la ruta de salida
    output_file <- file.path(ruta_out, 'Convocatorias_describe.csv')
    
    # Exportamos el csv 
    write.csv(descriptivos, file = output_file)
    
    # Mensaje del save exitoso
    cat("La descripción se ha guardado en", output_file, "\n") 
    
    
##### ----- OSCE_Lista sancionados_SAIP -------- #######
    
    data_cons <- read_excel(paste0(ruta, 'OSCE_Lista sancionados_SAIP.xlsx'))
    
    # Seleccionamos solo variables numéricas
    data_numeric <- data_cons[, sapply(data_cons, is.numeric)]
    
    # Realizamos el describe
    description <- psych::describe(data_numeric)
    
    # Calculamos los percentiles y el IQR para cada variable
    percentiles_iqr <- lapply(data_numeric, function(x) {
      quantiles <- quantile(x, c(0.25, 0.75), na.rm = TRUE)
      iqr_value <- IQR(x, na.rm = TRUE)
      c(quantiles[1], quantiles[2], IQR = iqr_value)
    })
    
    # Convertimos la lista de resultados a un dataframe
    percentiles_iqr_df <- as.data.frame(do.call(rbind, percentiles_iqr))
    
    # Juntamos los describe con los percentiles en un nuevo dataframe
    descriptivos <- cbind(description, percentiles_iqr_df)
    
    # Apuntamos a la ruta de salida
    output_file <- file.path(ruta_out, 'OSCE_Lista sancionados_SAIP_describe.csv')
    
    # Exportamos el csv 
    write.csv(descriptivos, file = output_file)
    
    # Mensaje del save exitoso
    cat("La descripción se ha guardado en", output_file, "\n")  

    
##### ----- Ranking_INCO_ent-reg -------- #######
    
    data_cons <- read_excel(paste0(ruta, 'Ranking_INCO_ent-reg.xlsx'))
    
    # Seleccionamos solo variables numéricas
    data_numeric <- data_cons[, sapply(data_cons, is.numeric)]
    
    # Realizamos el describe
    description <- psych::describe(data_numeric)
    
    # Calculamos los percentiles y el IQR para cada variable
    percentiles_iqr <- lapply(data_numeric, function(x) {
      quantiles <- quantile(x, c(0.25, 0.75), na.rm = TRUE)
      iqr_value <- IQR(x, na.rm = TRUE)
      c(quantiles[1], quantiles[2], IQR = iqr_value)
    })
    
    # Convertimos la lista de resultados a un dataframe
    percentiles_iqr_df <- as.data.frame(do.call(rbind, percentiles_iqr))
    
    # Juntamos los describe con los percentiles en un nuevo dataframe
    descriptivos <- cbind(description, percentiles_iqr_df)
    
    # Apuntamos a la ruta de salida
    output_file <- file.path(ruta_out, 'Ranking_INCO_ent-reg_describe.csv')
    
    # Exportamos el csv 
    write.csv(descriptivos, file = output_file)
    
    # Mensaje del save exitoso
    cat("La descripción se ha guardado en", output_file, "\n")  
    