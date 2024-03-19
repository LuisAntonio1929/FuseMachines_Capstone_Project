from sklearn.neural_network import MLPRegressor, MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler, Binarizer
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import pickle
from plot_result import plot_result
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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

posNN = MLPRegressor(hidden_layer_sizes=[50,200,50,10,50,200,50], tol=1e-2, max_iter=500, random_state=0)
posNN.fit(Xp_train[:,:3], yp_train).score(Xp_test[:,:3], yp_test)

pickle.dump(posNN, open('posNN.sav', 'wb'))

negNN = Pipeline([('scaler', MinMaxScaler(feature_range=(-1,1))),('mlp', MLPRegressor(hidden_layer_sizes=[100]*10, tol=1e-4, max_iter=1000, random_state=0))])
negNN.fit(Xn_train, yn_train[:,3:]).score(Xn_test, yn_test[:,3:])

pickle.dump(negNN, open('negNN.sav', 'wb'))

yp_pred = posNN.predict(Xp_test[:,:3])

rmse = np.sqrt(np.mean((yp_test-yp_pred)**2, axis=0))
print(rmse)

yn_pred = negNN.predict(Xn_test)

rmse = np.sqrt(np.mean((yn_test-yn_pred)**2, axis=0))
print(rmse)

fig = make_subplots(rows=2, cols=2, specs=[[{'type': 'scene'}, {'type': 'scene'}],
                                           [{'type': 'scene'}, {'type': 'scene'}]])

fig.add_trace(go.Scatter3d(
            x=yp_test[:5000,3],
            y=yp_test[:5000,4],
            z=yp_test[:5000,5],
            mode='markers',
            name='y_test',
            marker=dict(size=3,
                        color="red"),
            ),row=1, col=1)

fig.add_trace(go.Scatter3d(
            x=yp_pred[:5000,3],
            y=yp_pred[:5000,4],
            z=yp_pred[:5000,5],
            mode='markers',
            name='y_pred',
            marker=dict(size=3,
                        color="green"),
            ),row=1, col=1)

fig.add_trace(go.Scatter3d(
            x=yp_test[:5000,0],
            y=yp_test[:5000,1],
            z=yp_test[:5000,2],
            mode='markers',
            name='y_test',
            marker=dict(size=3,
                        color="red"),
            ),row=1, col=2)

fig.add_trace(go.Scatter3d(
            x=yp_pred[:5000,0],
            y=yp_pred[:5000,1],
            z=yp_pred[:5000,2],
            mode='markers',
            name='y_pred',
            marker=dict(size=3,
                        color="green"),
            ),row=1, col=2)

fig.add_trace(go.Scatter3d(
            x=yp_pred[:5000,3]-yp_test[:5000,3],
            y=yp_pred[:5000,4]-yp_test[:5000,4],
            z=yp_pred[:5000,5]-yp_test[:5000,5],
            mode='markers',
            name='y_pred',
            marker=dict(size=3,
                        color=yp_pred[:5000,5]-yp_test[:5000,5],
                        colorscale='Viridis',
                        ),
            ),row=2, col=1)

fig.add_trace(go.Scatter3d(
            x=yp_pred[:5000,0]-yp_test[:5000,0],
            y=yp_pred[:5000,1]-yp_test[:5000,1],
            z=yp_pred[:5000,2]-yp_test[:5000,2],
            mode='markers',
            name='y_test',
            marker=dict(size=3,
                        color=yp_pred[:5000,2]-yp_test[:5000,2],
                        colorscale='Viridis',
                        ),
            ),row=2, col=2)




# Set layout
fig.update_layout(
    height=1000,
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

fig = make_subplots(rows=2, cols=2, specs=[[{'type': 'scene'}, {'type': 'scene'}],
                                           [{'type': 'scene'}, {'type': 'scene'}]])

fig.add_trace(go.Scatter3d(
            x=yn_test[:5000,3],
            y=yn_test[:5000,4],
            z=yn_test[:5000,5],
            mode='markers',
            name='y_test',
            marker=dict(size=3,
                        color="red"),
            ),row=1, col=1)

fig.add_trace(go.Scatter3d(
            x=yn_pred[:5000,3],
            y=yn_pred[:5000,4],
            z=yn_pred[:5000,5],
            mode='markers',
            name='y_pred',
            marker=dict(size=3,
                        color="green"),
            ),row=1, col=1)

fig.add_trace(go.Scatter3d(
            x=yn_test[:5000,0],
            y=yn_test[:5000,1],
            z=yn_test[:5000,2],
            mode='markers',
            name='y_test',
            marker=dict(size=3,
                        color="red"),
            ),row=1, col=2)

fig.add_trace(go.Scatter3d(
            x=yn_pred[:5000,0],
            y=yn_pred[:5000,1],
            z=yn_pred[:5000,2],
            mode='markers',
            name='y_pred',
            marker=dict(size=3,
                        color="green"),
            ),row=1, col=2)

fig.add_trace(go.Scatter3d(
            x=yn_pred[:5000,3]-yn_test[:5000,3],
            y=yn_pred[:5000,4]-yn_test[:5000,4],
            z=yn_pred[:5000,5]-yn_test[:5000,5],
            mode='markers',
            name='y_pred',
            marker=dict(size=3,
                        color=yn_pred[:5000,5]-yn_test[:5000,5],
                        colorscale='Viridis',
                        ),
            ),row=2, col=1)

fig.add_trace(go.Scatter3d(
            x=yn_pred[:5000,0]-yn_test[:5000,0],
            y=yn_pred[:5000,1]-yn_test[:5000,1],
            z=yn_pred[:5000,2]-yn_test[:5000,2],
            mode='markers',
            name='y_test',
            marker=dict(size=3,
                        color=yn_pred[:5000,2]-yn_test[:5000,2],
                        colorscale='Viridis',
                        ),
            ),row=2, col=2)




# Set layout
fig.update_layout(
    height=1000,
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

plot_result(yp_test,yp_pred)

plot_result(yn_test,yn_pred)

