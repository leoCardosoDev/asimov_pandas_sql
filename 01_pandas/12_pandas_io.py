import pandas as pd

df1 = pd.read_csv('01_pandas/exemplo.csv', sep=',', decimal='.')
print(df1)
print(df1.info())
df1.to_csv('01_pandas/output.csv', sep=';', decimal=',')