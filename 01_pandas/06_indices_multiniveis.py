import pandas as pd
import numpy as np

# Níveis de indice
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3, 1,2,3]
hierarquia_index = list(zip(outside, inside))
print(hierarquia_index)
print()
hier_index = pd.MultiIndex.from_tuples(hierarquia_index)
print(hier_index)
df = pd.DataFrame(np.random.randn(6,2), index=hier_index, columns=['A', 'B'])
print(df)
print()
print(df.loc['G1'])
print(df.loc['G1'].loc[1])
print(df.index.names)
df.index.names = ['Grupo', 'Número']
print(df)
print(df.xs('G1'))
print(df.xs(1, level='Número'))
