import plotly.express as px
from pathlib import Path

folder = Path(__file__).parent
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig.write_html(folder / 'first_figure.html', auto_open=True)
