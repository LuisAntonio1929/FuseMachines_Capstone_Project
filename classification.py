from sklearn.model_selection import train_test_split
from sklearn.neural_network import BernoulliRBM
from sklearn.preprocessing import StandardScaler, MinMaxScaler, Binarizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.svm import SVC

import numpy as np

import pandas as pd

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import pickle

porcentaje_de_datos_para_entrenamiento = 90 

# Variables de trabajo

train_percent = porcentaje_de_datos_para_entrenamiento/100

df = pd.read_excel('data.xlsx')

c = df[['c1','c2','c3','c4','c5','c6']]
dr1r2 = df[["dr1r2"]]
theta1 = df[["theta1"]]
theta2 = df[["theta2"]]

y = c
#X = np.hstack((dr1r2[..., np.newaxis],theta1[..., np.newaxis]**2,theta2[..., np.newaxis]**2,theta1[..., np.newaxis],theta2[..., np.newaxis],dv1v2[..., np.newaxis]))
#X = np.hstack((dr1r2[..., np.newaxis],theta1[..., np.newaxis]**2,theta2[..., np.newaxis]**2,theta1[..., np.newaxis],theta2[..., np.newaxis],dw1v2[..., np.newaxis],dw2v1[..., np.newaxis]))
X = np.hstack((dr1r2[..., np.newaxis],theta1[..., np.newaxis],theta2[..., np.newaxis]))

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_percent, random_state=100)

bool_mask_train = y_train[:,2]>0
bool_mask_test = y_test[:,2]>0

mask_train = bool_mask_train*1
mask_test = bool_mask_test*1

Xp_train = X_train[bool_mask_train]
Xp_test = X_test[bool_mask_test]

Xn_train = X_train[~bool_mask_train]
Xn_test = X_test[~bool_mask_test]

yp_train = y_train[bool_mask_train]
yp_test = y_test[bool_mask_test]

yn_train = y_train[~bool_mask_train]
yn_test = y_test[~bool_mask_test]

mask = Pipeline([('scaler', StandardScaler()),('svc', SVC(C=10000))])
mask.fit(X_train[:,:3], mask_train).score(X_test[:,:3], mask_test)

pickle.dump(mask, open('mask.sav', 'wb'))
loaded_mask = pickle.load(open('mask.sav', 'rb'))

mask_pred = mask.predict(X_test[:,:3])

bool_mask_pred = np.array(mask_pred, dtype=bool)
ConfusionMatrixDisplay.from_predictions(mask_test, mask_pred)

fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'scene'}, {'type': 'scene'}]])

fig.add_trace(go.Scatter3d(
            x=y_test[:5000,0],
            y=y_test[:5000,1],
            z=y_test[:5000,2],
            mode='markers',
            name='true',
            marker=dict(size=3,
                        color=mask_test[:5000],
                        showscale=True,
                        colorscale='viridis',
                        colorbar=dict(len=1.05, x=1.1 ,y=0.49),
                        ),
            ),row=1, col=1)

fig.add_trace(go.Scatter3d(
            x=y_test[:5000,0],
            y=y_test[:5000,1],
            z=y_test[:5000,2],
            mode='markers',
            name='pred',
            marker=dict(size=3,
                        color=mask_pred[:5000],
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
