import plotly.graph_objects as go

fig = go.Figure(data=go.Heatmap(
    z=[[1, None, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
    x=['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
    y=['Manhã', 'Tarde', 'Noite'],
))

fig.show()
