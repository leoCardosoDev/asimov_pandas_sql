import plotly.graph_objects as go

labels = ['Oxigênio', 'Hidrogênio', 'Gás Carbônico', 'Nitrogênio']
values = [4500, 2500, 1053, 500]

fig = go.Figure(
    data=go.Pie(labels=labels, values=values, pull=[0, 0, 0.03, 0])
)

fig.update_traces(hoverinfo="label+value")

fig.show()
