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
print(pd.to_datetime(df['DATA INICIAL']))
print(pd.to_datetime(df['DATA FINAL']))
print(type(pd.to_datetime(df['DATA INICIAL'])[2]))
print(pd.to_datetime(df['DATA INICIAL'])[2])
print(pd.to_datetime(df['DATA INICIAL'])[2].day)
print(pd.to_datetime(df['DATA INICIAL'])[2].month)
print(pd.to_datetime(df['DATA INICIAL'])[2].year)
print(pd.to_datetime(df['DATA INICIAL'])[2].week)
print(pd.to_datetime(df['DATA INICIAL'])[2].weekday)

# 5. Crie uma nova coluna para representar o ano e o mês (aaaa-mm), utilizando 
# a coluna 'DATA FINAL' como referência
print(pd.to_datetime(df['DATA FINAL']))
df['ANO-MES'] = pd.to_datetime(df['DATA FINAL']).apply(lambda x: '{}'.format(x.year)) + pd.to_datetime(df['DATA FINAL']).apply(lambda x: '/{:02d}'.format(x.month))
print(df['ANO-MES'])

# 6. Utilizando values_counts(), liste os tipos de produtos contidos na base de dados
print(df.columns)
print(df['PRODUTO'].value_counts())

# 7. Filtre o Dataframe para obter apenas dados da 'GASOLINA COMUM'. Grave em uma nova variável
df_filtro = df['PRODUTO'] == 'GASOLINA COMUM'
df3 = df[df_filtro]
print(df3)

# 8. Qual o preço médio de revenda da gasolina em Agosto de 2008
df_2008_08 = df3[df3['ANO-MES'] == '2008/08']
print(df_2008_08['PREÇO MÉDIO REVENDA'].mean())

# 9. Qual o preço médio de revenda da gasolina em Maio de 2014 em São Paulo
print(df3[(df3['ANO-MES'] == '2014/05') & (df3['ESTADO'] == 'SAO PAULO')]['PREÇO MÉDIO REVENDA'].mean())

# 10. Você conseguiria descobrir em qual(quais) estados(s) a gasolina 
# ultrapassou a barreira dos R$ 5,00? E quando isso ocorreu?
print(df3[df3['PREÇO MÉDIO REVENDA'] > 5].columns)
print(df3[df3['PREÇO MÉDIO REVENDA'] > 5][['ESTADO', 'ANO-MES', 'PREÇO MÉDIO REVENDA']])

# 11. Qual o preço médio dos estados da região sul em 2012?
df_aux = df3[pd.to_datetime(df3['DATA FINAL']).apply(lambda x: x.year) == 2012]
print(df_aux[df_aux['REGIÃO'] == "SUL"]['PREÇO MÉDIO REVENDA'].mean())

