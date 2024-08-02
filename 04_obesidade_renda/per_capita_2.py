import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# Leitura do arquivo CSV
folder = Path(__file__).parent
df_gdp = pd.read_csv(folder / 'gdp.csv')

# Limpeza e Conversão dos Dados
df_gdp['Year'] = df_gdp['Year'].apply(lambda x: int(x.split('/')[-1]))
df_gdp['gdp_pp'] = df_gdp[' GDP_pp '].apply(lambda x: float(x.strip().replace(',', '')))
del df_gdp[' GDP_pp ']

# Identificação dos anos disponíveis e criação de um índice completo de anos
all_years = range(df_gdp['Year'].min(), df_gdp['Year'].max() + 1)

# Criar um DataFrame com todos os anos para cada país
countries = df_gdp['Country'].unique()
df_full_index = pd.MultiIndex.from_product([countries, all_years], names=['Country', 'Year'])
df_full = pd.DataFrame(index=df_full_index).reset_index()

# Merge com o DataFrame original para identificar anos ausentes
df_gdp_full = pd.merge(df_full, df_gdp, on=['Country', 'Year'], how='left')

# Interpolação dos valores ausentes
df_gdp_full['gdp_pp'] = df_gdp_full.groupby('Country')['gdp_pp'].apply(lambda group: group.interpolate()).reset_index(level=0, drop=True)

# Verificar se ainda existem valores ausentes
print(df_gdp_full.isnull().sum())

# Validação dos dados interpolados
# Aqui, podemos verificar visualmente ou usar estatísticas para garantir que os dados interpolados fazem sentido
for country in countries:
    df_country = df_gdp_full[df_gdp_full['Country'] == 'Brazil']
    plt.figure(figsize=(10, 5))
    plt.plot(df_country['Year'], df_country['gdp_pp'], marker='o')
    plt.title(f'GDP per Capita Interpolation for {country}')
    plt.xlabel('Year')
    plt.ylabel('GDP per Capita')
    plt.show()
