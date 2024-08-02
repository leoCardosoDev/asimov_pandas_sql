import plotly.express as px
import seaborn as sns
import pandas as pd

# Carregando o conjunto de dados 'tips' do Seaborn
tips = sns.load_dataset('tips')

# Criando um gráfico de dispersão
fig = px.scatter(tips, x='total_bill', y='tip', color='sex', title='Total Bill vs Tip')
fig.show()

# Criando um gráfico de barras
fig = px.bar(tips, x='day', y='total_bill', color='sex', title='Total Bill by Day and Sex')
fig.show()

# Criando um histograma
fig = px.histogram(tips, x='total_bill', nbins=30, title='Distribution of Total Bill')
fig.show()

# Dados de exemplo
data = {
    'Date': pd.date_range(start='1/1/2020', periods=10),
    'Value': [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]
}
df = pd.DataFrame(data)

# Criando um gráfico de linha
fig = px.line(df, x='Date', y='Value', title='Value Over Time')
fig.show()

# Criando um box plot
fig = px.box(tips, x='day', y='total_bill', color='sex', title='Total Bill Distribution by Day and Sex')
fig.show()

# Criando um gráfico de violino
fig = px.violin(tips, x='day', y='total_bill', color='sex', title='Total Bill Distribution by Day and Sex')
fig.show()

# Dados de exemplo de localizações
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Latitude': [40.7128, 34.0522, 41.8781, 29.7604, 33.4484],
    'Longitude': [-74.0060, -118.2437, -87.6298, -95.3698, -112.0740],
    'Population': [8419000, 3980400, 2716000, 2328000, 1690000]
}
df = pd.DataFrame(data)

# Criando um gráfico de mapa
fig = px.scatter_geo(df, lat='Latitude', lon='Longitude', text='City', size='Population', title='City Populations in the USA')
fig.show()


