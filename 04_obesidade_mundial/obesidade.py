from pathlib import Path
import pandas as pd
import numpy as np

current_folder = Path(__file__).parent
df_obesity = pd.read_csv(current_folder / 'obesity_cleaned.csv')

# 1. Limpe os dados do Dataframe, criando uma coluna de nome 'Obesity' 
# que conterá os valores de obesidade. Transforme em float as colunas 
# que porventura foram importadas como string
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
