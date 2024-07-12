from pathlib import Path
import pandas as pd

pasta_atual = Path(__file__).parent
df_data = pd.read_csv(pasta_atual / 'supermarket_sales.csv')

# 1. Qual o faturamento total por filial
faturamento_total_por_filial = df_data.groupby('City')['Total'].sum()
print(faturamento_total_por_filial)