import pandas as pd

# Dados de exemplo
data = {
    'Classe': ['Júnior', 'Júnior', 'Pleno', 'Pleno', 'Sênior', 'Sênior'],
    'Nome': ['Jorge', 'Carlos', 'Roberta', 'Patrícia', 'Bruno', 'Vera'],
    'Venda': [200, 120, 340, 124, 243, 350],
}
df = pd.DataFrame(data)
print(df)

print()
print("**"*25)
print()

print('# Selecionando apenas as colunas numéricas para as operações de agregação')
df_numerico = df.select_dtypes(include=['number'])


print('# Adicionando a coluna "Classe" de volta para o agrupamento')
df_numerico['Classe'] = df['Classe']

print(df_numerico.groupby("Classe").sum())
print()
print(df_numerico.groupby("Classe").mean())
print()
print(df_numerico.groupby("Classe").min())
print()
print(df_numerico.groupby("Classe").max())

print()
print("**"*25)
print()
