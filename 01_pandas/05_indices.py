import pandas as pd
import numpy as np
from numpy.random import randn

# DataFrame
df = pd.DataFrame(randn(5,4), index=['A', 'B', 'C', 'D', 'E'], columns='W X Y Z'.split())
df['new'] = df['W'] + df['Y']

print(df.index)
print(df.columns)
print(df.reset_index())
print(df)
print(df.reset_index(inplace=True))
print(df)
print("___---___"*10)
print(df.set_index('index', inplace=True))
print(df)
print()
print("==__--"*10)
print()
novo_indice = 'CA NY WY OR CO'.split()
print(novo_indice)
df['novo_indice'] = novo_indice
print(df)
print()
print(df.reset_index().set_index('novo_indice'))
df.set_index('novo_indice', inplace=True)
print(df)
