from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=1, cols=2)

fig.add_trace(go.Bar(y=[1, 4, 5], x=[6,5,2], marker_color='blue'), row=1, col=1)
fig.add_trace(go.Scatter(y=[7, 6, 5, 4], x=[4,3,2,1], marker_color='blue'), row=1, col=2)
fig.update_layout(title_text='Usando o update_layout', title_font_size=20)

fig.show()
