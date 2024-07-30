import seaborn as sns
import matplotlib.pyplot as plt
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Carregando o conjunto de dados
tips = sns.load_dataset('tips')

# Criando um KDE plot para a coluna 'total_bill'
sns.kdeplot(tips['total_bill'], fill=True)
plt.title('KDE Plot da Conta Total')
plt.xlabel('Conta Total')
plt.ylabel('Densidade')
plt.show()