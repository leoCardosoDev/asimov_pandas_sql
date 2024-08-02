from pathlib import Path
import pandas as pd

pasta_atual = Path(__file__).parent
df_data = pd.read_csv(pasta_atual / 'supermarket_sales.csv')

print()
print('-_-'*55)
print()

# 1. Qual o faturamento total por filial
faturamento_total_por_filial = df_data.groupby('City')[['Total', 'gross income']].sum()
print(faturamento_total_por_filial)

print()
print('-_-'*55)
print()

# 2. Qual o percentual de participação na receita de cada tipo de produto?
percentual_receita = (df_data.groupby('Product line')['Total'].sum() / df_data.groupby('Product line')['Total'].sum().sum()).sort_values() * 100
print(percentual_receita)

print()
print('-_-'*55)
print()

# 3. Como está distribuido o tipo de produto consumido por genero?
by_genre = df_data.groupby(['Product line', 'Gender'])[['Total']].sum().pivot_table(index='Product line', columns='Gender')
print(by_genre)

print()
print('-_-'*55)
print()

# 4. Qual foi o faturamento por mês?
df_data['Date'] = pd.to_datetime(df_data['Date'])
df_data['Month'] = df_data['Date'].apply(lambda x: x.month)
df_data['Year'] = df_data['Date'].apply(lambda x: x.year)
faturamento_mes = df_data.groupby(['Month'])['Total'].sum()
print(faturamento_mes)

print()
print('-_-'*55)
print()

# 5. Qual foi a média de avaliação por cada filial em Janeiro de 2019
rating = df_data[(df_data['Year'] == 2019) & (df_data['Month'] == 1)]['Rating'].mean()
print(rating)

print()
print('-_-'*55)
print()

# 5. Como se distribui o gasto por tipo de consumidor em cada filial?
consumer = df_data.groupby(['Customer type', 'City'])['Total'].sum()
print(consumer)

print()
print('-_-'*55)
print()
