import plotly.graph_objects as go
import pandas as pd

# Exemplo de dados fictícios para o gráfico de Candlestick
data = {
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Open': [100, 102, 104, 103, 105, 108, 110, 112, 115, 117],
    'High': [102, 105, 106, 107, 110, 111, 113, 116, 118, 120],
    'Low': [98, 100, 102, 101, 103, 107, 109, 111, 114, 115],
    'Close': [101, 104, 105, 106, 109, 110, 112, 115, 117, 119]
}

df = pd.DataFrame(data)

# Criando o gráfico de Candlestick
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close']
)])

# Adicionando título e rótulos
fig.update_layout(
    title='Exemplo de Gráfico de Candlestick',
    xaxis_title='Data',
    yaxis_title='Preço',
    xaxis_rangeslider_visible=False
)

# Exibindo o gráfico
fig.show()
