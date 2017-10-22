'''
Created on Oct 22, 2017

@author: leandrolopes
'''

import pandas as pd
import numpy as np
from pandas.tests.io.parser import parse_dates, usecols
#from matplotlib.pyplot import style

#style.use('ggplot')

web_stats = { 'Dia': [1,2,3,4,5,6],
              'Visitantes' : [23,43,12,23,4,5],
              'Clicks': [123,543,564,124,1234,555]}

file = "./data/DADOS_GERAIS.csv"
qtde = 50000

#Teste de identificação de colunas
#cols = pd.read_csv(file, nrows=1).columns
#print(cols)


#Parser para a Data
#parser = lambda x: pd.datetime.strptime(x, '%y:%j:%???')
#df = pd.read_csv(file, error_bad_lines=False,parse_dates=['DataCadastro'], date_parser=parser, dtype={'IdSKU': np.int64, 'CodigoMktp': object, 'Ean13': object} , sep=";",header=0 , infer_datetime_format=True, nrows=qtde, encoding='latin-1')                     

df = pd.read_csv(file, error_bad_lines=False, dtype={'IdSKU': np.int64, 'CodigoMktp': object, 'Ean13': object} , sep=";",header=0 , infer_datetime_format=True, nrows=qtde, encoding='latin-1')                     
             
print(df)
print(df.dtypes)


#print(df.head(1))
#print(df.tail(1))

