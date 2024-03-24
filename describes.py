import pandas as pd
import numpy as np

# Ruta de trabajo
ruta = "C:/Users/llore/R/Proyectos/Sunat/"
ruta_out = "C:/Users/llore/R/Proyectos/Sunat"

# Leer el archivo Excel
data_cons = pd.read_excel(ruta + 'Adjudicaciones.xlsx')

# Seleccionar solo variables numéricas
data_numeric = data_cons.select_dtypes(include=[np.number])

# Realizar el describe
description = data_numeric.describe()

# Calculamos los percentiles y el IQR para cada variable
percentiles_iqr = data_numeric.apply(lambda x: [np.percentile(x, 25), np.percentile(x, 75), np.percentile(x, 75) - np.percentile(x, 25)], axis=0)

# Convertir los resultados a un DataFrame
percentiles_iqr_df = pd.DataFrame(percentiles_iqr.values, columns=['25%', '75%', 'IQR'], index=percentiles_iqr.index)

# Juntar los describe con los percentiles en un nuevo DataFrame
descriptivos = pd.concat([description, percentiles_iqr_df], axis=1)

# Guardar el resultado en un archivo CSV
output_file = ruta_out + '/Adjudicaciones_describe.csv'
descriptivos.to_csv(output_file)

# Mensaje de éxito
print("La descripción se ha guardado en", output_file)
