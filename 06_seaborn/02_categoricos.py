import seaborn as sns
import matplotlib.pyplot as plt
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Carregando o conjunto de dados
tips = sns.load_dataset('tips')

