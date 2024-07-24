from pathlib import Path
import pandas as pd
import numpy as np

current_folder = Path(__file__).parent
df_obesity = pd.read_csv(current_folder / 'obesity_cleaned.csv')

# Questão 1
print('''1. Limpe os dados do Dataframe, criando uma coluna de nome 'Obesity' que conterá os valores de obesidade. Transforme em float as colunas que porventura foram importadas como string''')
print(df_obesity.columns)
del df_obesity['Unnamed: 0']
print(df_obesity['Country']) # object (string)
print(df_obesity['Year']) # int64
print(df_obesity['Obesity (%)']) # object (string) -limpar campos vazios -converter para float
print(df_obesity['Sex']) # object (string)
print('\nTrabalhando com a coluna Obesity (%)')
print(df_obesity['Obesity (%)'].iloc[0]) # retorno = 0.5 [0.2-1.1]
print(df_obesity['Obesity (%)'].value_counts()) # No data 504
df_obesity['Obesity (%)'].iloc[0].split()
df_obesity['Obesity'] = df_obesity['Obesity (%)'].apply(lambda x: x.split()[0])
print(df_obesity['Obesity'].value_counts()) # No 504
df_obesity.loc[df_obesity['Obesity'] == 'No', 'Obesity'] = np.nan
df_obesity['Obesity'] = df_obesity['Obesity'].dropna()
print(df_obesity['Obesity']) # dtype: object
df_obesity['Obesity'] = df_obesity['Obesity'].apply(lambda x: float(x))
df_obesity['Year'] = df_obesity['Year'].apply(lambda x: int(x)) # Garantir que o Year seja int
print(df_obesity['Obesity']) # dtype: float64
df_obesity.set_index('Year', inplace=True)
print(df_obesity)

print('****'*30)
print('\n\n')
# Questão 2
print('2. Qual o percentual médio de obesidade por sexo no mundo no ano de 2015?')
media = df_obesity[df_obesity.index == 2015].groupby('Sex').mean(numeric_only=True)
print(media)

print('****'*30)
print('\n\n')
# Questão 3
print('Quais são os países com a maior e a meno taxa de aumento nos índices de obesidade no período observado?')
df_obesity_start = df_obesity[df_obesity.index == 1975]
df_obesity_end = df_obesity[df_obesity.index == 2016]
df_obesity_start.set_index('Country', inplace=True)
df_obesity_end.set_index('Country', inplace=True)
df_obesity_evolution = df_obesity_end[df_obesity_end['Sex'] == 'Both sexes']['Obesity'] - df_obesity_start[df_obesity_end['Sex'] == 'Both sexes']['Obesity']
print(df_obesity_evolution.sort_values().dropna().tail(5))
print(df_obesity_end[df_obesity_end.index == 'Tuvalu'])
