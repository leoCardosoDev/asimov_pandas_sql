import plotly.graph_objects as go

# Definindo os pontos (vértices) da malha
x = [0, 1, 2, 0, 1, 2, 0, 1, 2]
y = [0, 0, 0, 1, 1, 1, 2, 2, 2]
z = [0, 1, 0, 1, 2, 1, 0, 1, 0]

# Criando o gráfico de Mesh3D
fig = go.Figure(data=[go.Mesh3d(
    x=x,
    y=y,
    z=z,
    color='lightblue',
    opacity=0.50
)])

# Adicionando título e rótulos
fig.update_layout(
    title='Exemplo de Gráfico de Mesh3D',
    scene = dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    )
)

# Exibindo o gráfico
fig.show()
