import plotly.graph_objects as go
import numpy as np

np.random.seed(1)
x = np.random.randn(500)
y = np.random.randn(500) + 1

fig = go.Figure(go.Histogram2d(x=x, y=y))
fig.show()
