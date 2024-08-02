import sqlite3
import pandas as pd
from pathlib import Path
import os

db = Path(__file__).parent / 'web.db'
if db.exists():
    os.remove(db)
csv = Path(__file__).parent / 'bd_data.csv'
db = Path(__file__).parent / 'web.db'
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
# df_data2.to_sql('data', connection, if_exists='append')

# SELECT
commands.execute('SELECT * FROM data')
df = pd.DataFrame(commands.fetchall())
print(df)

# WHERE
commands.execute('SELECT * FROM data WHERE A > 200')
df2 = pd.DataFrame(commands.fetchall())
print(df2)
print('**__**'*20)
commands.execute('SELECT * FROM data WHERE A > 200 and B > 100')
df2 = pd.DataFrame(commands.fetchall())
print(df2)
print('**__**'*20)
commands.execute('SELECT A, B, C FROM data WHERE A > 200 and B > 100')
df2 = pd.DataFrame(commands.fetchall())
print(df2)

# Com Pandas
query = 'SELECT * FROM data'
df3 = pd.read_sql(query, con=connection, index_col='index_name')
print(f'\n{df3}\n')

df4 = pd.read_sql_query("SELECT A, B, C FROM data WHERE A > 200 and B > 100", con=connection)
print(f'\n{df4}\n')

# UPDATE e DELETE
commands.execute("UPDATE data SET A=219, Z=2.9 WHERE index_name='b'")
connection.commit()

# DELETE
commands.execute("DELETE FROM data WHERE index_name='b'")
connection.commit()
