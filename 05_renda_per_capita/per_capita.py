from pathlib import Path
import pandas as pd

folder = Path(__file__).parent
df_gdp = pd.read_csv(folder / 'gdp.csv')

# 1. Limpe o conjunto de dados, convertendo strings em datas, float ou int quando necessário
print(df_gdp.columns) # Index(['Country', 'Region', 'Year', ' GDP_pp '], dtype='object')
# Coluna 'Year'
print(type(df_gdp['Year'].iloc[0])) # str
df_gdp['Year'] = df_gdp['Year'].apply(lambda x: int(x.split('/')[-1]))
print(df_gdp['Year'])
# Coluna ' GDP_pp '
print(type(df_gdp[' GDP_pp '].iloc[0])) # str com espaços
print(df_gdp[' GDP_pp '].iloc[0]) #  613.99  com espaços em branco
print(df_gdp[' GDP_pp '].iloc[0].split()[0]) # 613.99
print(float(df_gdp[' GDP_pp '].iloc[0].split()[0])) # convert para float
df_gdp['gdp_pp'] = df_gdp[' GDP_pp '].apply(lambda x: float(x.split()[0].replace(',', '')))
del df_gdp[' GDP_pp ']
print(df_gdp)