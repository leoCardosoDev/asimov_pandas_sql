from pathlib import Path
import pandas as pd

folder = Path(__file__).parent
df_gdp = pd.read_csv(folder / 'gdp.csv')

# 1. Limpe o conjunto de dados, convertendo strings em datas, float ou int quando necessário
df_gdp.columns # Index(['Country', 'Region', 'Year', ' GDP_pp '], dtype='object')
# Coluna 'Year'
type(df_gdp['Year'].iloc[0]) # str
df_gdp['Year'] = df_gdp['Year'].apply(lambda x: int(x.split('/')[-1]))
df_gdp['Year']
# Coluna ' GDP_pp '
type(df_gdp[' GDP_pp '].iloc[0]) # str com espaços
df_gdp[' GDP_pp '].iloc[0] #  613.99  com espaços em branco
df_gdp[' GDP_pp '].iloc[0].split()[0] # 613.99
float(df_gdp[' GDP_pp '].iloc[0].split()[0]) # convert para float
df_gdp['gdp_pp'] = df_gdp[' GDP_pp '].apply(lambda x: float(x.split()[0].replace(',', '')))
del df_gdp[' GDP_pp ']

# 2. Você conseguiria informar o primeiro valor registrado de cada país?
df_first = df_gdp.groupby('Country')['Year'].min()
df_first = df_gdp.groupby('Country')['Year'].min().value_counts()
df_first = df_gdp.groupby('Country')['Year'].min().max()
df_first = df_gdp.groupby('Country')['Year'].min()[df_gdp.groupby('Country')['Year'].min() == 1991]

# 3. Informe as regiões com maiores crescimentos de PIB per capita no século passado
df_gdp_start = df_gdp[df_gdp['Year'] == 1901]
df_gdp[df_gdp['Year'] < 2000].max() # 1996
df_gdp_end = df_gdp[df_gdp['Year'] == 1996]
df_renda = ((df_gdp_end.groupby('Region')['gdp_pp'].mean() / df_gdp_start.groupby('Region')['gdp_pp'].mean() -1) * 100).sort_values()
print(df_renda)