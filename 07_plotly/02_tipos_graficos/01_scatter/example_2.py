import plotly.graph_objects as go
import numpy as np

N = 100
x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2= np.random.randn(N) - 5

fig = go.Figure()
fig.add_traces(go.Scatter(x=x, y=random_y0, mode='markers', name='markers'))
fig.add_traces(go.Scatter(x=x, y=random_y1, mode='lines+markers', name='lines+markers'))
fig.add_traces(go.Scatter(x=x, y=random_y2, mode='lines', name='lines'))
fig.show()
