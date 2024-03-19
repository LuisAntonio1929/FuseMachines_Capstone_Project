import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np


df = pd.read_excel('data.xlsx')

c = df[['c1','c2','c3','c4','c5','c6']]
dr1r2 = df[["dr1r2"]]
theta1 = df[["theta1"]]
theta2 = df[["theta2"]]

y = c
X = np.hstack((dr1r2[..., np.newaxis],theta1[..., np.newaxis],theta2[..., np.newaxis]))

# @title COEFICIENTES GRAFICA 1
fig = go.Figure(layout={'template':'plotly_dark'})
fig.add_trace(go.Scatter(y=c[:1000,0],
                         name='c1'))
fig.add_trace(go.Scatter(y=c[:1000,1],
                         name='c2'))
fig.add_trace(go.Scatter(y=c[:1000,2],
                         name='c3'))
fig.add_trace(go.Scatter(y=c[:1000,3],
                         name='c4'))
fig.add_trace(go.Scatter(y=c[:1000,4],
                         name='c5'))
fig.add_trace(go.Scatter(y=c[:1000,5],
                         name='c6'))

# Set layout
fig.update_layout(
    title_text=f"coeficientes",
    height=400,
    margin=dict(
        l=50,
        r=50,
        b=40,
        t=100,
        pad=4
    ),
)

# Add range slider
fig.update_layout(xaxis=dict(rangeslider=dict(visible=True)))

fig.show()