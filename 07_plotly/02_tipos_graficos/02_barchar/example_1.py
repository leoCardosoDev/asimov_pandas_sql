import plotly.graph_objects as go

animais = ['Girafas', 'Macacos', 'Tigres']

fig = go.Figure(
    data = [
        go.Bar(x=animais, y=[3, 120, 6], name='Zoo SP'),
        go.Bar(x=animais, y=[21, 40, 2], name='Zoo RS')
    ]
)

fig.update_layout(barmode='stack')

fig.show()