import sqlite3
import pandas as pd
from pathlib import Path

db = Path(__file__).parent / 'web.db'
csv = Path(__file__).parent / 'bd_data.csv'
connection = sqlite3.connect(db)
df_data = pd.read_csv(csv, index_col=0)
df_data.index.name = 'index_name'
df_data.to_sql('data', connection, index_label='index_name')

commands = connection.cursor()
commands.execute('CREATE TABLE products ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTERGER)')
# commands.execute('DROP TABLE products')
# commands.execute('DROP TABLE data')
connection.commit()
