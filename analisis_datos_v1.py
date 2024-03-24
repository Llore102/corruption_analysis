#!/usr/bin/env python
# coding: utf-8

# ## Librerias

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ## Ruta

# In[2]:


ruta_in = 'C:/Users/llore/R/Proyectos/Sunat/OSCE/'


# ## Convocatorias

# In[3]:


convocatorias_2019 = pd.read_excel(ruta_in + '1. CONOSCE_CONVOCATORIAS2019_0.xlsx')
convocatorias_2020 = pd.read_excel(ruta_in + '1. CONOSCE_CONVOCATORIAS2020_0703.xlsx')
convocatorias_2021 = pd.read_excel(ruta_in + '1. CONOSCE_CONVOCATORIAS2021_0.xlsx')
convocatorias_2022 = pd.read_excel(ruta_in + '1. CONOSCE_CONVOCATORIAS2022_0.xlsx')
convocatorias_2023 = pd.read_excel(ruta_in + '1. CONOSCE_CONVOCATORIAS2023_0.xlsx')


# In[4]:


convocatorias_2019.columns.values


# In[5]:


convocatorias_2020.columns.values


# In[6]:


convocatorias_2021.columns.values


# In[7]:


convocatorias_2022.columns.values


# In[8]:


convocatorias_2023.columns.values


# In[9]:


convocatorias = pd.concat([convocatorias_2019, convocatorias_2020, convocatorias_2021, convocatorias_2022, convocatorias_2023])
del([convocatorias_2019, convocatorias_2020, convocatorias_2021, convocatorias_2022, convocatorias_2023])


# In[10]:


convocatorias.shape


# In[11]:


condicion_pre_pandemia = (convocatorias['FECHA_CONVOCATORIA'] >= pd.Timestamp(2019, 1, 1)) & (convocatorias['FECHA_CONVOCATORIA'] < pd.Timestamp(2020, 3, 15))
condicion_pandemia = (convocatorias['FECHA_CONVOCATORIA'] >= pd.Timestamp(2020, 3, 16)) & (convocatorias['FECHA_CONVOCATORIA'] < pd.Timestamp(2022, 10, 1))
condicion_post_pandemia = (convocatorias['FECHA_CONVOCATORIA'] >= pd.Timestamp(2022, 10, 2))

convocatorias['FASE_PANDEMIA'] = np.where(condicion_pre_pandemia, 'pre_pandemia', 
                                    np.where(condicion_pandemia, 'pandemia', 'post_pandemia'))


# In[12]:


convocatorias.shape


# In[13]:


convocatorias['idx'] = convocatorias['CODIGOCONVOCATORIA'].astype(str).str.cat(convocatorias['N_ITEM'].astype(str), sep='-')


# In[14]:


convocatorias.head(2)


# In[15]:


convocatorias_T = convocatorias.groupby( ['TIPOENTIDAD', 'TIPO_COMPRA', 'TIPOPROCESOSELECCION', 'FASE_PANDEMIA'
                                          ]).agg({'ENTIDAD':'count'}).reset_index()
convocatorias_T


# In[16]:


convocatorias_p = convocatorias.groupby('TIPOENTIDAD').agg({'N_ITEM':'count'}).reset_index()
convocatorias_p


# In[73]:


convocatorias_por_tipo_entidad = convocatorias['TIPOENTIDAD'].value_counts()

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
convocatorias_por_tipo_entidad.plot(kind='bar')
plt.title('Número de Items por Tipo de Entidad')
plt.xlabel('Tipo de Entidad')
plt.ylabel('Número de Items')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Mostrar el gráfico
plt.show()


# In[18]:


convocatorias_o = convocatorias.groupby('OBJETOCONTRACTUAL').agg({'N_ITEM':'count'}).reset_index()
convocatorias_o


# In[74]:


convocatorias_por_objetivo_contractual = convocatorias['OBJETOCONTRACTUAL'].value_counts()

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
convocatorias_por_objetivo_contractual.plot(kind='bar')
plt.title('Número de Items por Objetivo contractual')
plt.xlabel('Objetivo contractual')
plt.ylabel('Número de Items')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Mostrar el gráfico
plt.show()


# In[20]:


convocatorias_tp = convocatorias.groupby('TIPO_COMPRA').agg({'N_ITEM':'count'}).reset_index()
convocatorias_tp


# In[75]:


convocatorias_por_tipo_compra = convocatorias['TIPO_COMPRA'].value_counts()

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
convocatorias_por_tipo_compra.plot(kind='bar')
plt.title('Número de Items por Tipo de compra')
plt.xlabel('Tipo de compra')
plt.ylabel('Número de Items')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Mostrar el gráfico
plt.show()


# In[22]:


convocatorias_sc = convocatorias.groupby('SECTOR').agg({'N_ITEM':'count'}).reset_index()
convocatorias_sc


# In[76]:


convocatorias_por_sector = convocatorias['SECTOR'].value_counts()

# Crear el gráfico de barras
plt.figure(figsize=(12, 8))

convocatorias_por_sector.plot(kind='bar')
plt.title('Número de Items por Sector')
plt.xlabel('Tipo de sector')
plt.ylabel('Número de Items')
plt.xticks(rotation=45, ha='right')
# Establecer el eje y con incrementos de 20,000
plt.tight_layout()

# Mostrar el gráfico
plt.show()


# In[24]:


convocatorias_tc = convocatorias.groupby('SISTEMA_CONTRATACION').agg({'N_ITEM':'count'}).reset_index()
convocatorias_tc


# In[77]:


convocatorias_por_sistema_contratacion = convocatorias['SISTEMA_CONTRATACION'].value_counts()

# Crear el gráfico de barras
plt.figure(figsize=(12, 8))

convocatorias_por_sistema_contratacion.plot(kind='bar')
plt.title('Número de Items por Tipo de sistema de contratación')
plt.xlabel('Tipo de sitema de contratacion')
plt.ylabel('Número de Items')
plt.xticks(rotation=45, ha='right')
# Establecer el eje y con incrementos de 20,000
plt.tight_layout()

# Mostrar el gráfico
plt.show()


# In[26]:


convocatorias_ts = convocatorias.groupby('TIPOPROCESOSELECCION').agg({'N_ITEM':'count'}).reset_index()
convocatorias_ts


# In[78]:


convocatorias_por_tipo_select = convocatorias['TIPOPROCESOSELECCION'].value_counts()

# Crear el gráfico de barras
plt.figure(figsize=(12, 8))
bars = convocatorias_por_tipo_select.plot(kind='bar', color='skyblue')

convocatorias_por_tipo_select.plot(kind='bar')
plt.title('Número de Items por Tipo de proceso de seleccion')
plt.xlabel('Tipo de compra')
plt.ylabel('Número de Items')
plt.xticks(rotation=45, ha='right')
# Establecer el eje y con incrementos de 20,000
plt.yticks(range(0, convocatorias_por_tipo_select.max() + 20000, 20000))
plt.tight_layout()

# Mostrar el gráfico
plt.show()


# In[28]:


convocatorias_cd = convocatorias.groupby(['CODIGOCONVOCATORIA', 'ENTIDAD']).agg({'N_ITEM':'count'}).reset_index()
convocatorias_cd


# In[29]:


convocatorias_e = convocatorias.groupby('ENTIDAD').agg({'N_ITEM':'count'}).reset_index()
convocatorias_e


# In[30]:


item_c = convocatorias[(convocatorias['CODIGOCONVOCATORIA'] == 431034)]
item_c


# In[31]:


data_numeric = convocatorias.select_dtypes(include=[np.number])

description = data_numeric.describe()

def calculate_percentiles_iqr(column):
    quantiles = column.quantile([0.25, 0.75])
    iqr_value = quantiles[0.75] - quantiles[0.25]
    return pd.Series([quantiles[0.25], quantiles[0.75], iqr_value], index=['25%', '75%', 'IQR'])

percentiles_iqr_df = data_numeric.apply(calculate_percentiles_iqr)

descriptivos = pd.concat([description, percentiles_iqr_df], axis=1)

descriptivos


# ## Postores

# In[32]:


postores_2019 = pd.read_excel(ruta_in + '2. CONOSCE_POSTOR2019_0.xlsx')
postores_2020 = pd.read_excel(ruta_in + '2. CONOSCE_POSTOR2020_0703.xlsx')
postores_2021 = pd.read_excel(ruta_in + '2. CONOSCE_POSTOR2021_0.xlsx')
postores_2022 = pd.read_excel(ruta_in + '2. CONOSCE_POSTOR2022_0.xlsx')
postores_2023 = pd.read_excel(ruta_in + '2. CONOSCE_POSTOR2023_0.xlsx')


# In[33]:


postores_2019.columns.values


# In[34]:


postores_2020.columns.values


# In[35]:


postores_2021.columns.values


# In[36]:


postores_2022.columns.values


# In[37]:


postores_2022.columns.values


# In[38]:


postores = pd.concat([postores_2019, postores_2020, postores_2021, postores_2022, postores_2023])
del([postores_2019, postores_2020, postores_2021, postores_2022, postores_2023])


# In[39]:


postores.shape


# In[40]:


postores['idx'] = postores['CODIGO_CONVOCATORIA'].astype(str).str.cat(postores['N_ITEM'].astype(str), sep='-')


# In[41]:


postores.shape


# In[42]:


postores.head(2)


# In[43]:


postores_p = postores.groupby('POSTOR').agg({'N_ITEM':'count'}).reset_index()
postores_p


# In[44]:


postores_cd = postores.groupby(['CODIGO_CONVOCATORIA', 'POSTOR']).agg({'N_ITEM':'count'}).reset_index()
postores_cd


# In[45]:


item_p = postores[(postores['CODIGO_CONVOCATORIA'] == 431034)]
item_p


# ## Adjudicados

# In[46]:


adjudicados_2019 = pd.read_excel(ruta_in + '3. CONOSCE_ADJUDICACIONES2019_0.xlsx')
adjudicados_2020 = pd.read_excel(ruta_in + '3. CONOSCE_ADJUDICACIONES2020_0703.xlsx')
adjudicados_2021 = pd.read_excel(ruta_in + '3. CONOSCE_ADJUDICACIONES2021_0.xlsx')
adjudicados_2022 = pd.read_excel(ruta_in + '3. CONOSCE_ADJUDICACIONES2022_0.xlsx')
adjudicados_2023 = pd.read_excel(ruta_in + '3. CONOSCE_ADJUDICACIONES2023_0.xlsx')


# In[47]:


adjudicados_2019.columns.values


# In[48]:


adjudicados_2020.columns.values


# In[49]:


adjudicados_2021.columns.values


# In[50]:


adjudicados_2022.columns.values


# In[51]:


adjudicados_2023.columns.values


# In[52]:


adjudicados = pd.concat([adjudicados_2019, adjudicados_2020, adjudicados_2021, adjudicados_2022, adjudicados_2023])
del([adjudicados_2019, adjudicados_2020, adjudicados_2021, adjudicados_2022, adjudicados_2023])


# In[53]:


adjudicados.tail(10)


# In[54]:


adjudicados.shape


# In[55]:


adjudicados['idx'] = adjudicados['CODIGOCONVOCATORIA'].astype(str).str.cat(adjudicados['N_ITEM'].astype(str), sep='-')


# In[56]:


adjudicados.shape


# ## Contratos

# In[57]:


contratos_2019 = pd.read_excel(ruta_in + '5. CONOSCE_CONTRATOS2019_0.xlsx')
contratos_2020 = pd.read_excel(ruta_in + '5. CONOSCE_CONTRATOS2020_0703.xlsx')
contratos_2021 = pd.read_excel(ruta_in + '5. CONOSCE_CONTRATOS2021_0.xlsx')
contratos_2022 = pd.read_excel(ruta_in + '5. CONOSCE_CONTRATOS2022_0.xlsx')
contratos_2023 = pd.read_excel(ruta_in + '5. CONOSCE_CONTRATOS2023_0.xlsx')


# In[58]:


contratos_2019.columns.values


# In[59]:


contratos_2020.columns.values


# In[60]:


contratos_2021.columns.values


# In[61]:


contratos_2022.columns.values


# In[62]:


contratos_2023.columns.values


# In[63]:


contratos = pd.concat([contratos_2019, contratos_2020, contratos_2021, contratos_2022, contratos_2023])
del([contratos_2019, contratos_2020, contratos_2021, contratos_2022, contratos_2023])


# In[64]:


contratos.shape


# In[65]:


contratos['idx'] = contratos['CODIGOCONVOCATORIA'].astype(str).str.cat(contratos['NUM_ITEM'].astype(str), sep='-')


# In[66]:


contratos.shape


# In[ ]:




