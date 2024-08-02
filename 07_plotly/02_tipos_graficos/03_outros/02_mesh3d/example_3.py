import plotly.graph_objects as go
import numpy as np

# Dados fictícios do bairro do Engenho Novo em Barueri, SP
# Coordenadas de latitude e longitude (convertidas para valores numéricos) e altitude
latitudes = np.array([37.7749, 37.7740, 37.7750, 37.7760, 37.7770, 37.7780])
longitudes = np.array([-122.4194, -122.4190, -122.4180, -122.4170, -122.4160, -122.4150])
altitudes = np.array([10, 20, 15, 25, 10, 20])  # Exemplo de elevações

# Normalizando as latitudes e longitudes para valores apropriados
x = latitudes - latitudes.min()
y = longitudes - longitudes.min()
z = altitudes

# Criando o gráfico Mesh3D
fig = go.Figure(data=[go.Mesh3d(
    x=x,
    y=y,
    z=z,
    color='lightgreen',
    opacity=0.50
)])

# Adicionando título e rótulos
fig.update_layout(
    title='Gráfico Mesh3D do Bairro Engenho Novo em Barueri, SP',
    scene=dict(
        xaxis_title='Latitude (normalizada)',
        yaxis_title='Longitude (normalizada)',
        zaxis_title='Altitude (m)'
    )
)

# Exibindo o gráfico
fig.show()
