import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np


df = pd.read_excel('data.xlsx')

c = df[['c1','c2','c3','c4','c5','c6']]
dr1r2 = df[["dr1r2"]]

fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'scene'}, {'type': 'scene'}]])

fig.add_trace(go.Scatter3d(
            x=c[:5000,3],
            y=c[:5000,4],
            z=c[:5000,5],
            mode='markers',
            name='c_345',
            marker=dict(size=3,
                        color=dr1r2[:5000],
                        showscale=True,
                        colorscale='Viridis',
                        colorbar=dict(len=1.05, x=0.4 ,y=0.49),
                        ),
            ),row=1, col=1)

fig.add_trace(go.Scatter3d(
            x=c[:5000,0],
            y=c[:5000,1],
            z=c[:5000,2],
            mode='markers',
            name='c_012',
            marker=dict(size=3,
                        color=(c[:5000,2]>0)*1,
                        showscale=True,
                        colorscale='viridis',
                        colorbar=dict(len=1.05, x=1.1 ,y=0.49),
                        ),
            ),row=1, col=2)


# Set layout
fig.update_layout(
    height=500,
    margin=dict(
        l=50,
        r=50,
        b=40,
        t=100,
        pad=4
    ),
)

# Add range slider
fig.update_layout(xaxis=dict(rangeslider=dict(visible=True)),
                  template='plotly_dark')

fig.show()