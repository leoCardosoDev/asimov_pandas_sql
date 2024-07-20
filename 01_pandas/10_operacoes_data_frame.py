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
