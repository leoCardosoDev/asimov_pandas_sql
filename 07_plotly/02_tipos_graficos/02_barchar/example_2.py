import plotly.graph_objects as go

items = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E']
qtd = [20, 14, 23, 25, 22]
colors = ['lightslategray'] * 5
colors[1] = 'green'

fig = go.Figure(
    data=[
        go.Bar(x=items, y=qtd, marker_color=colors)
    ])

fig.show()
