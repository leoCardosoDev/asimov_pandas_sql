import plotly.graph_objects as go
import numpy as np

np.random.seed(1)

y0 = np.random.randn(50) - 1
y1 = np.random.randn(50) + 1

fig = go.Figure()
fig.add_trace(go.Box(x=y0))
fig.add_trace(go.Box(x=y1))

fig.show()
