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
# Create
commands.execute('CREATE TABLE products ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTERGER)')
# Insert
commands.execute('''
    INSERT INTO products (product_id, product_name, price)
    VALUES
    (1, "Computer", 800),
    (2, "Printer", 200),
    (3, "Tablet", 300)
''')
connection.commit()

# Inserindo com pandas
df_data2 = df_data.iloc[::-2]
df_data2.to_sql('data', connection, if_exists='append')
