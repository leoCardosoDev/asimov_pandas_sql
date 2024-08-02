import plotly.graph_objects as go
import numpy as np

x = np.random.randn(500)
x1 = np.random.randn(500) + 1
fig = go.Figure()
fig.add_trace(go.Histogram(x=x))
fig.add_trace(go.Histogram(x=x1))

fig.update_layout(barmode='overlay')
fig.update_traces(opacity=0.75)

fig.show()
