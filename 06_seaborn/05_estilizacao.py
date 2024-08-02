import seaborn as sns
import matplotlib.pyplot as plt
import ssl

# Desativando a verificação SSL (não recomendado para produção)
ssl._create_default_https_context = ssl._create_unverified_context

# Carregando o conjunto de dados
tips = sns.load_dataset('tips')

# Aplicando o estilo 'whitegrid'
sns.set_style('whitegrid')

# Criando um boxplot para 'total_bill' categorizado por 'day' com estilo aplicado
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title('Boxplot da Conta Total por Dia com Estilo Whitegrid')
plt.xlabel('Dia')
plt.ylabel('Conta Total')
plt.show()

# Aplicando uma paleta de cores
sns.set_palette('pastel')

# Criando um violinplot para 'total_bill' categorizado por 'day' com paleta aplicada
sns.violinplot(x='day', y='total_bill', data=tips)
plt.title('Violinplot da Conta Total por Dia com Paleta Pastel')
plt.xlabel('Dia')
plt.ylabel('Conta Total')
plt.show()
