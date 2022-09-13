"""
MIT License

Copyright (c) 2022 UnB

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import plotly.express as px # type: ignore
from pandas import DataFrame

from data_migrator import df
from utils import filter_columns

def create_chart(df: DataFrame, labels: dict, config: dict = {}): # type: ignore
    chart = px.line( # type: ignore
        df,
        x="year",
        y="net_migrants",
        color="region",
        line_shape="linear",
        labels=labels,
        markers=True,
    )

    chart.update_layout(config)
    return chart

# Aqui definimos as configurações de layout do gráfico.
config = {"title": {"text": "Taxa de Migração (1955-2020)","x": 0.5}}
labels = {"year": "Ano", "net_migrants": "Migrantes", "region": "Região"}

# A criação do gráfico utiliza o modo "linear" do Plotly.
# Alguns itens básicos foram alterados, como a representação
# das "etiquetas" de ano, imigrantes e região.
filtered_df = filter_columns(df, "year", "net_migrants", "region")

# Aqui criamos o gráfico utilizando a função `create_chart`
chart = create_chart(filtered_df, labels, config)