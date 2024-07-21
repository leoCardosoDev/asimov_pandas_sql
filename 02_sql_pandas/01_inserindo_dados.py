import sqlite3
import pandas as pd
from pathlib import Path

db = Path(__file__).parent / 'web.db'
csv = Path(__file__).parent / 'bd_data.csv'
connection = sqlite3.connect(db)
df_data = pd.read_csv(csv, index_col=0)
print(df_data)
