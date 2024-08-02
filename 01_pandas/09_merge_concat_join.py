import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1','A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0,1,2,3])


df2 = pd.DataFrame({'A': ['A4', 'A5','A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[4,5,6,7])


df3 = pd.DataFrame({'A': ['A8', 'A9','A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8,9,10,11])

print(f'{df1}\n')
print(f'{df2}\n')
print(f'{df3}\n')

print(f'{pd.concat([df1, df2, df3])}\n')
print(f'{pd.concat([df1, df2, df3], axis=1)}\n')


esquerda = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})

direita = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})

print(f'{esquerda}\n')
print(f'{direita}\n')

print(f'{pd.merge(esquerda, direita, on="key")}\n')

esquerda2 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                        'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})

direita2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                        'key2': ['K0', 'K0', 'K0', 'K0'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})

print(f'Esquerda: \n{esquerda2}\n')
print(f'Direita: \n{direita2}\n')

print(f'{pd.merge(esquerda2, direita2, on=["key1", "key2"])}\n')
# print(f'{pd.merge(esquerda2, direita2, how='cross', on=["key1", "key2"])}')
print(f'{pd.merge(esquerda2, direita2, how='inner', on=["key1", "key2"])}\n')
print(f'{pd.merge(esquerda2, direita2, how='left', on=["key1", "key2"])}\n')
print(f'{pd.merge(esquerda2, direita2, how='outer', on=["key1", "key2"])}\n')
print(f'{pd.merge(esquerda2, direita2, how='right', on=["key1", "key2"])}\n')

esquerda3 = pd.DataFrame({'A': ['A0', 'A1','A2'],
                    'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])

direita3 = pd.DataFrame({'C': ['C0', 'C2','C3'],
                    'D': ['D0', 'D2', 'D3']},
                    index=['K0', 'K2', 'K3'])

print(f'{esquerda3}\n')
print(f'{direita3}\n')
print(f'{esquerda3.join(direita3)}\n')
print(f'{esquerda3.join(direita3, how='left')}\n')
print(f'{esquerda3.join(direita3, how='outer')}\n')
print(f'{esquerda3.join(direita3, how='right')}\n')
