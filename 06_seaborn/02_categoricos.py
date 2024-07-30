import seaborn as sns
import matplotlib.pyplot as plt
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Carregando o conjunto de dados
tips = sns.load_dataset('tips')

# Criando um boxplot para a coluna 'total_bill' categorizada por 'day'
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title('Boxplot da Conta Total por Dia')
plt.xlabel('Dia')
plt.ylabel('Conta Total')
plt.show()