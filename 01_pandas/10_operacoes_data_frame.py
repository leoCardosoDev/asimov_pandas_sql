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

print(f'Soma: {df['col1'].sum()}')
print(f'Media: {df['col1'].mean()}')
print(f'Produto: {df['col1'].product()}')
print(f'Desvio padrão: {df['col1'].std()}')
print(f'Máximo: {df['col1'].max()}')
print(f'Minimo: {df['col1'].min()}')
print(f'Indice do máximo: {df['col1'].idxmax()}')
print(f'Indice do mínimo: {df['col1'].idxmin()}')

print(f'\n{df[df['col2'] == 444]}\n')
print(f'{df[df['col2'] == 444]['col1'].sum()}\n')

print(f'\n{df.sort_values(by='col2')}\n')

data = {'A':['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B':['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
        'D':[1,3,2,5,4,1]}
df2 = pd.DataFrame(data)
print(f'\n{df2}\n')
dict_map = {'one': '1', 'two': 2}
print(df2['B'].map(dict_map))
df2['E'] = df2['B'].map(dict_map)
print(f'{df2}\n')

print(f'\n{df2.pivot_table(index="A", columns="B", values="D")}\n')
