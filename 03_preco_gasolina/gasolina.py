import pandas as pd
from pathlib import Path

pasta_atual = Path(__file__).parent

# 1. Carregue os conjuntos de dados "gasolina_2000+.csv" em 
# dois Dataframes diferentes e combine-os em um unico Dataframe
df1 = pd.read_csv(pasta_atual / 'gasolina_2000+.csv', index_col=0)
df2 = pd.read_csv(pasta_atual / 'gasolina_2010+.csv', index_col=0)
df = pd.concat([df1, df2])
print(df1.shape)
print(df2.shape)
print(df.shape)

# 2. Investigue as colunas e entenda o conjunto de dados usando o head() e info()
print(df.head())
print(df.info())
print(df.tail())
print(df['MARGEM MÉDIA REVENDA'][0])

# 3. Selecione a terceira entrada da coluna DATA INICIAL e verifique o seu tipo
print(df['DATA INICIAL'][2])
print(type(df['DATA INICIAL'][2]))

# 4. Você deve ter percebido que as colunas 'DATA INICIAL' e 'DATA FINAL' 
# estão formatadas como string. Utilizando o método pd.to_datetime(), converta 
# ambas as colunas para Timestamp/Datetime
pd.to_datetime(df['DATA INICIAL'])
pd.to_datetime(df['DATA FINAL'])
print(type(df['DATA INICIAL'][2]))