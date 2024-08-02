import pandas as pd
import numpy as np
from numpy.random import randn


# DataFrame
df = pd.DataFrame(randn(5,4), index=['A', 'B', 'C', 'D', 'E'], columns='W X Y Z'.split())
print(df)
print(type(df))
print(df['W'])
print(df[['W']])

df['new'] = df['W'] + df['Y']
print(df)
print(df[['new']])
df2 = df.drop('new', axis=1)
print(df)
df.drop('new', axis=1, inplace=True)
print(df)
print(df.loc['A'])
print(df.loc[['A']])
print(df.iloc[0, 2])
