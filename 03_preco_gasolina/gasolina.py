import pandas as pd
from pathlib import Path

pasta_atual = Path(__file__).parent

# 1. Carregue os conjuntos de dados "gasolina_2000+.csv" em 
# dois Dataframes diferentes e combine-os em um unico Dataframe
df1 = pd.read_csv(pasta_atual / 'gasolina_2000+.csv')
