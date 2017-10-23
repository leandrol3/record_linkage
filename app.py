'''
Created on Oct 22, 2017

@author: leandrolopes
'''

import pandas as pd
import numpy as np
import recordlinkage


from pandas.tests.io.parser import parse_dates, usecols
from nameparser import HumanName
from bokeh.layouts import column

HumanName('Leandro Cesar Lopes')
#from matplotlib.pyplot import style

#style.use('ggplot')

#web_stats = { 'Dia': [1,2,3,4,5,6],
#             'Visitantes' : [23,43,12,23,4,5],
#              'Clicks': [123,543,564,124,1234,555]}

file = "./data/DADOS_GERAIS.csv"
qtde = 4000000


#Teste de identificação de colunas
#cols = pd.read_csv(file, nrows=1).columns
#print(cols)

#Index(['IdSKU;CodigoMktp;DataCadastro;Produto;IdCategoria;Categoria;IdDepartamento;Departamento;Ean13;Qtde_Disponivel;Ult_Data_movimento_Estoque;Vendas_Ano;Vendas_Mes_Anterior'], dtype='object')


#Parser para a Data
#parser = lambda x: pd.datetime.strptime(x, '%y:%j:%???')
#df = pd.read_csv(file, error_bad_lines=False,parse_dates=['DataCadastro'], date_parser=parser, dtype={'IdSKU': np.int64, 'CodigoMktp': object, 'Ean13': object} , sep=";",header=0 , infer_datetime_format=True, nrows=qtde, encoding='latin-1')                     

df = pd.read_csv(file, error_bad_lines=False, usecols=[0,1,3,6,7,8], dtype={'IdSKU': np.int64, 'CodigoMktp': object, 'Ean13': object} , sep=";",header=0 , infer_datetime_format=True, nrows=qtde, encoding='latin-1')                     
          

#df_EAN_Unique = df.duplicated(['Ean13'], keep=False)
df_EAN_Unique = pd.DataFrame(df.duplicated(['Ean13'], keep=False))

df_Title_Unique = pd.DataFrame(df.duplicated(['Produto'], keep=False))  
#df_Title_Unique = df.duplicated(['Produto'], keep=False)  

#print(df_EAN_Unique)    #9833
#df_REGRA1 = pd.DataFrame(df_EAN_Unique, df_Title_Unique}, columns=['EAN', 'Title'])

#print(df_REGRA1.shape)

#print(df_Title_Unique)  #9298

#df_REGRA1 = pd.({df_EAN_Unique,df_Title_Unique}, dtype=bool)
      
#print(df_REGRA1)

df_Title_Attribute_Unique = df.duplicated(['Produto', 'CodigoMktp'], keep=False)
print(df_Title_Attribute_Unique)


