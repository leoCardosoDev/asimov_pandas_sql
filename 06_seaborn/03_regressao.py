import seaborn as sns
import matplotlib.pyplot as plt
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Carregando o conjunto de dados
tips = sns.load_dataset('tips')

# Criando um regplot para 'total_bill' e 'tip'
sns.regplot(x='total_bill', y='tip', data=tips)
plt.title('Regplot da Conta Total e Gorjeta')
plt.xlabel('Conta Total')
plt.ylabel('Gorjeta')
plt.show()
