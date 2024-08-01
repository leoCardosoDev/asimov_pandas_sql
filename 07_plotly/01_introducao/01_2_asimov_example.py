import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(x=[1,2,3], y=[3,2,1])],
    layout=go.Layout(title={'text': 'Uma figura especifica por um objeto de gráfico'})
)
fig.show()
