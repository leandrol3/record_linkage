'''
Created on Oct 22, 2017

@author: leandrolopes
'''

import pandas as pd
import numpy as np
import recordlinkage


from pandas.tests.io.parser import parse_dates, usecols
from nameparser import HumanName
#from layouts import column

#HumanName('Leandro Cesar Lopes')
#from matplotlib.pyplot import style

#style.use('ggplot')

#web_stats = { 'Dia': [1,2,3,4,5,6],
#             'Visitantes' : [23,43,12,23,4,5],
#              'Clicks': [123,543,564,124,1234,555]}

file = "./data/DADOS_GERAIS.csv"
qtde = 40000


#Teste de identificação de colunas
#cols = pd.read_csv(file, nrows=1).columns
#print(cols)

#Index(['IdSKU;CodigoMktp;DataCadastro;Produto;IdCategoria;Categoria;IdDepartamento;Departamento;Ean13;Qtde_Disponivel;Ult_Data_movimento_Estoque;Vendas_Ano;Vendas_Mes_Anterior'], dtype='object')


#Parser para a Data
#parser = lambda x: pd.datetime.strptime(x, '%y:%j:%???')
#df = pd.read_csv(file, error_bad_lines=False,parse_dates=['DataCadastro'], date_parser=parser, dtype={'IdSKU': np.int64, 'CodigoMktp': object, 'Ean13': object} , sep=";",header=0 , infer_datetime_format=True, nrows=qtde, encoding='latin-1')                     

#Carrega o arquivo dados_gerais  
df = pd.read_csv(file, error_bad_lines=False, usecols=[0,1,3,6,7,8], dtype={'IdSKU': np.int64, 'CodigoMktp': object, 'Ean13': object} , sep=";",header=0 , infer_datetime_format=True, nrows=qtde, encoding='latin-1')                     
          
#Aplicação da Regra 1.1 - Identifica EAN e depois Titulos Duplicados
df_EAN_Duplicated = df.duplicated(['Ean13'], keep=False)
df_Title_Duplicated = pd.DataFrame(df.duplicated(['Produto'], keep=False))  

df['Ean_Duplicated'] = df_EAN_Duplicated
df['Title_Duplicated'] = df_Title_Duplicated

#Aplicação da Regra 1.2 - Identifica Titulos e Atributos Duplicados
df_Title_Attribute_Unique = df.duplicated(['Produto', 'CodigoMktp'], keep=False)

df['Title_Attribute_Duplicated'] = df_Title_Attribute_Unique


# Separa os itens que serão marcados em Azul
#(tips['time'] == 'Dinner') & (tips['tip'] > 5.00)]
df_UNIQUE = (df['Ean_Duplicated'] == True)  # & (df['Title_Duplicated'] == True)

print(df_UNIQUE)





