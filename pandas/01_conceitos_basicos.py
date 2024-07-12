from pathlib import Path
import pandas as pd

pasta_atual = Path(__file__).parent
df_data = pd.read_csv(pasta_atual / 'supermarket_sales.csv')

