import plotly.graph_objects as go
import numpy as np

t = np.linspace(0, 10, 100)
y = np.sin(t)

fig = go.Figure(
    data=go.Scatter(x=t, y=y, mode='lines')
)

fig.show()
