import pandas as pd
import numpy as np

labels = ['a', 'b', 'c']
minha_lista = [10, 20, 30]
arr = np.array([10, 20, 30])
dic = {'a': 10, 'b': 20, 'c': 30}
simples = pd.Series(labels)
print(simples)
print()
print('_-_-_'*30)
print()

completo = pd.Series(data=labels, index=minha_lista)
# completo = pd.Series(labels, minha_lista)
print(completo)
print()
print('_-_-_'*30)
print()

print(pd.Series(dic))

print()
print('_-_-_'*30)
print()

series1 = pd.Series([1, 2, 3, 4], index=['EUA', 'Alemanha', 'Rússia', 'Japão'])
print(series1)

series2 = pd.Series([1, 2, 3, 4], index=['EUA', 'Alemanha', 'Itália', 'Japão'])
print(series2)

print(series1['EUA'])
print(series1[['EUA', 'Rússia']])
print(series1 + series2)
