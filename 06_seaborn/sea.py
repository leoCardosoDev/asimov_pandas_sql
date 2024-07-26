import certifi
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

## Capítulo 1: Introdução ao Seaborn
### 1.3 Primeiro Gráfico com Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando um conjunto de dados de exemplo
data = sns.load_dataset('iris')

# Criando um gráfico de dispersão
sns.scatterplot(data=data, x='sepal_length', y='sepal_width', hue='species')
plt.title('Scatter Plot of Iris Dataset')
plt.show()

## Capítulo 2: Gráficos Simples com Seaborn
### 2.1 Histogramas
sns.histplot(data['sepal_length'], kde=True)
plt.title('Histogram of Sepal Length')
plt.show()

### 2.2 Jointplots
sns.jointplot(data=data, x='sepal_length', y='sepal_width', kind='scatter')
plt.suptitle('Joint Plot of Sepal Length and Sepal Width', y=1.02)
plt.show()

### 2.3 Pairplots
sns.pairplot(data, hue='species')
plt.suptitle('Pair Plot of Iris Dataset', y=1.02)
plt.show()

## Capítulo 3: Gráficos Categóricos
### 3.1 Boxplots
sns.boxplot(data=data, x='species', y='sepal_length')
plt.title('Box Plot of Sepal Length by Species')
plt.show()

### 3.2 Barplots
sns.barplot(data=data, x='species', y='sepal_length')
plt.title('Bar Plot of Sepal Length by Species')
plt.show()

### 3.3 Violinplots
sns.violinplot(data=data, x='species', y='sepal_length')
plt.title('Violin Plot of Sepal Length by Species')
plt.show()

### 3.4 Swarmplots
sns.swarmplot(data=data, x='species', y='sepal_length')
plt.title('Swarm Plot of Sepal Length by Species')
plt.show()

## Capítulo 4: Gráficos Avançados
### 4.1 Lmplots
sns.lmplot(data=data, x='sepal_length', y='sepal_width', hue='species')
plt.title('LM Plot of Sepal Length vs Sepal Width')
plt.show()

### 4.2 Heatmaps
# Selecionando apenas as colunas numéricas
numeric_data = data.select_dtypes(include='number')
# Calculando a matriz de correlação
correlation_matrix = numeric_data.corr()

# Criando um heatmap com a matriz de correlação
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap of Iris Dataset Correlation Matrix')
plt.show()

### 4.3 Clustermaps
# Selecionando apenas as colunas numéricas
numeric_data = data.select_dtypes(include='number')
# Calculando a matriz de correlação
correlation_matrix = numeric_data.corr()
# Criando um clustermap com a matriz de correlação
sns.clustermap(correlation_matrix, annot=True, cmap='coolwarm')
# Exibindo o gráfico
plt.title('Clustermap of Correlation Matrix')
plt.show()



