import plotly.graph_objects as go
import pandas as pd
import ssl

# Desativando a verificação SSL (não recomendado para produção)
ssl._create_default_https_context = ssl._create_unverified_context
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure(
    data=[go.Candlestick(
        x = df['Date'],
        open=df['AAPL.Open'],
        high=df['AAPL.High'],
        low=df['AAPL.Low'],
        close=df['AAPL.Close']
    )]
)
fig.show()
