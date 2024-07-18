import pandas as pd
import numpy as np
from numpy.random import randn

# DataFrame
df = pd.DataFrame(randn(5,4), index=['A', 'B', 'C', 'D', 'E'], columns='W X Y Z'.split())
df['new'] = df['W'] + df['Y']
df2 = df.drop('new', axis=1)
df.drop('new', axis=1, inplace=True)
print(df.loc[['A', 'B']])
print(df.loc[['A', 'B'], 'W'])
print()
print(df)
print()
print(df.iloc[0, 2])
print()
print(df.iloc[:-1, :])
print()
print(df.iloc[:-1, 1:4])
print()
print(df > 0)
print()
print(df[df>0])
print()
print(df[df['Y'] > 0])
print()
print(df[(df['Y'] > 0) & (df['W'] > 0)])
