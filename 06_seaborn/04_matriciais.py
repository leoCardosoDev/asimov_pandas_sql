import seaborn as sns
import matplotlib.pyplot as plt
import ssl

# Desativando a verificação SSL (não recomendado para produção)
ssl._create_default_https_context = ssl._create_unverified_context

# Carregando o conjunto de dados
tips = sns.load_dataset('tips')

# Selecionando apenas as colunas numéricas
numeric_cols = tips.select_dtypes(include=['float64', 'int64'])

# Calculando a matriz de correlação
corr = numeric_cols.corr()

# Criando um heatmap com a matriz de correlação
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Heatmap da Matriz de Correlação')
plt.show()
