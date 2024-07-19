import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1,2, np.nan],
    'B': [5, np.nan, np.nan],
    'C': [1, 2, 3]
})
print(df)

print()
print("**"*25)
print()

print(df.dropna())
print(df.dropna(axis=0))
print(df.dropna(axis=1))
print(df.dropna(axis=1, thresh=2))

print()
print("**"*25)
print()

print(df.fillna(0))
print(df.fillna('0'))
print(df['A'].sum())
print(df['A'].mean())
print(df['A'].fillna(value=df['A'].sum()))
print(df['A'].fillna(value=df['A'].mean()))

print()
print("**"*25)
print()


