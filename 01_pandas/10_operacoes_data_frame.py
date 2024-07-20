import pandas as pd

df = pd.DataFrame({'col1': [1,2,3,4], 'col2': [444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xvz']})
print(f'{df.head()}\n')
print(f'{df.info()}\n')
print(f'{df.memory_usage()}\n')
print(f'{df['col2'].unique()}\n')
print(f'{df['col2'].nunique()}\n')
print(f'{df['col2'].value_counts()}\n')
print(f'{df['col2'].value_counts().index}\n')

def computacao(x):
    return x ** 2 + 3
print(f'\n{df}\n')
print(f'{df["col1"].apply(computacao)}\n')
df['col1_calc'] = df['col1'].apply(computacao)
print(f'\n{df['col1_calc']}\n')
print(f'\n{df['col2'].apply(lambda x: x ** 2 + 3)}\n')