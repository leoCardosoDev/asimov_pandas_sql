from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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


# 4. Preencha os anos ausentes em cada pais com uma estimativa, baseada na diferença entre o proximo registro e o anterior
arr_year = np.arange(df_gdp['Year'].min(), df_gdp['Year'].max())
df_all_years = pd.DataFrame(arr_year, columns=['Year'])
df_all_years.index = df_all_years['Year']
df_years_off = ~df_all_years['Year'].isin(df_gdp['Year'])
df_years_off = df_all_years.loc[df_years_off].index
df_gdp = df_gdp.sort_values(['Country', 'Year'])
df_gdp['delta_gdp'] = df_gdp['gdp_pp'] - df_gdp['gdp_pp'].shift(1)
df_gdp['delta_year'] = df_gdp['Year'] - df_gdp['Year'].shift(1)
df_gdp['gdp_year'] = (df_gdp['delta_gdp'] / df_gdp['delta_year']).shift(-1)
df_gdp['next_year'] = df_gdp['Year'].shift(-1)
del df_gdp['delta_gdp'], df_gdp['delta_year']
df_new_data = pd.DataFrame()
for idx, row in df_gdp.iterrows():
    if row['Year'] == 2011:
        continue
    years_to_add = df_years_off[(df_years_off < row['next_year']) & (df_years_off >row['Year'])]
    for new_year in years_to_add:
        add_row = row.copy()
        add_row['gdp_pp'] = (new_year - add_row['Year']) * add_row['gdp_pp'] + add_row['gdp_pp']
        add_row['Year'] = new_year
        add_row['kind'] = 'estimated'
        df_new_data = pd.concat([df_new_data, add_row.to_frame().transpose()])
df_gdp = pd.concat([df_gdp, df_new_data])
df_gdp.sort_values(['Country', 'Year'], inplace=True)
df_gdp.index = df_gdp['Year']
df_gdp['kind'].fillna('real', inplace=True)

fig, ax = plt.subplots(figsize=(20,5))
country = 'Brazil'
df_gdp[(df_gdp['kind'] == 'real') & (df_gdp['Country'] == country)].plot(kind='scatter', y='gdp_pp', x="Year", ax=ax)
df_gdp[(df_gdp['kind'] == 'estimated') & (df_gdp['Country'] == country)].plot(kind='scatter', y='gdp_pp', x="Year", ax=ax, color="red")
plt.show()
