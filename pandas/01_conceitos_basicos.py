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