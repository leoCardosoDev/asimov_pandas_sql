import pandas as pd
import datetime

numeros_de_dias = 100
datas = pd.date_range(start='1/1/2021', periods=numeros_de_dias)
print(f'{datas}\n')

df = pd.DataFrame(range(numeros_de_dias), columns=['number'], index=datas)
print(f'{df}\n')
print(f'{df.index}\n')
print(f'{df.index[0]}\n')
print(f'{df.index[0].day}\n')
print(f'{df.index[0].month}\n')
print(f'{df.index[0].year}\n')
print(f'{df.index[0].hour}\n')

print(f'{df[df.index.month == 1]}\n')
print(f'{df[df.index.day == 10]}\n')
df['Month'] = df.index.month
print(f'{df}\n')

print(f'{df[df.index > datetime.datetime(2021, 1, 10)]}')
