import numpy as np
from vectors import spherical_vector, linear_vector
from transformations import lie_bracket_t, t_2_SE3, SE3_2_t
import plotly.graph_objects as go
import pickle

ndim = 3 #numero de dimensiones

def test_gen():
  #vectores de rotacion (screws)
  w1 = spherical_vector(ndim)
  w2 = spherical_vector(ndim)

  #puntos de aplicacion del screw
  q1 = linear_vector(ndim)
  q2 = linear_vector(ndim)

  #expresion en se3 para velocidad lineal en rotacion pura
  v1 = np.cross(-w1,q1)
  v2 = np.cross(-w2,q2)

  #vector R6 de se3
  wv1 = np.concatenate((w1,v1))
  wv2 = np.concatenate((w2,v2))

  return wv1, wv2

wv1, wv2 = test_gen()
tx,ty = np.linspace(-np.pi, np.pi, 40), np.linspace(-np.pi, np.pi, 40)
u,v = np.meshgrid(tx,ty)

mask = pickle.load(open('mask.sav', 'rb'))
posNN = pickle.load(open('posNN.sav', 'rb'))
negNN = pickle.load(open('negNN.sav', 'rb'))

def metric_gen(theta1,theta2):
  t1 = theta1/np.pi
  t2 = theta2/np.pi

  #primeros 6 componentes de Baker–Campbell–Hausdorff formula
  r1 = wv1*t1
  r2 = -wv2*t2
  r12 = lie_bracket_t(r1,r2)
  r112 = lie_bracket_t(r1,r12)
  r221 = lie_bracket_t(r2,-r12)
  r2112 = lie_bracket_t(r2,r112)

  WV = np.stack((r1,r2,r12,r112,r221,r2112), axis=1)

  #producto escalar
  dw1w2 = np.dot(r1[:3],r2[:3])

  #signo de c3:
  mask_pred = mask.predict([np.concatenate(([dw1w2],[t1**2],[t2**2]))])
  #prediccion:

  if mask_pred[0] > 0:
    c_pred = posNN.predict([np.concatenate(([dw1w2],[t1**2],[t2**2]))])
  else:
    c_pred = negNN.predict([np.concatenate(([dw1w2],[t1],[t2]))])

  c_pred = np.ravel(c_pred)
  r3 = WV@c_pred

  #metricas
  m1 = np.dot(r3,r3)
  m2 = np.dot(r3[3:],r3[:3]) + np.dot(r3[:3],r3[3:])

  return m1,m2

def matrix_gen(theta1,theta2):
  t1 = theta1/np.pi
  t2 = theta2/np.pi

  #primeros 6 componentes de Baker–Campbell–Hausdorff formula
  r1 = wv1*t1
  r2 = wv2*t2
  r12 = lie_bracket_t(r1,r2)
  r112 = lie_bracket_t(r1,r12)
  r221 = lie_bracket_t(r2,-r12)
  r2112 = lie_bracket_t(r2,r112)

  #producto escalar
  dw1w2 = np.dot(r1[:3],r2[:3])
  dv1v2 = np.dot(r1[3:],r2[3:])

  #composicion de transformaciones
  TH1 = t_2_SE3(wv1,theta1)
  TH2 = t_2_SE3(wv2,theta2)
  TH3 = TH1@TH2
  wv3,theta3 = SE3_2_t(TH3)

  r3_true = wv3*theta3/np.pi

  #calculo de coeficientes Ax=b
  #matriz A
  A = np.vstack((r1,r2,r12,r112,r221,r2112)).T

  #coeficientes "x"
  c_true = np.linalg.pinv(A) @ r3_true

  #signo de c3:
  mask_pred = mask.predict([np.concatenate(([dw1w2],[t1**2],[t2**2]))])
  #prediccion:

  if mask_pred[0] > 0:
    c_pred = posNN.predict([np.concatenate(([dw1w2],[t1**2],[t2**2]))])
  else:
    c_pred = negNN.predict([np.concatenate(([dw1w2],[t1**2],[t2**2],[t1],[t2],[dv1v2]))])

  c_pred = np.ravel(c_pred)

  c_true_norm = np.linalg.norm(c_true)
  c_pred_norm = np.linalg.norm(c_pred)
  cos_sim = np.dot(c_true,c_pred)/(c_true_norm*c_pred_norm)

  return cos_sim,c_true_norm,c_pred_norm

func = np.vectorize(matrix_gen)
mfunc = np.vectorize(metric_gen)
result = func(u,v)
mresult = mfunc(u,v)

# METRICA 1

fig = go.Figure(layout={'template':'plotly_dark'})

fig.add_trace(go.Surface(z=mresult[0], x=tx, y=ty))

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

fig.show()

# METRICA 2

fig = go.Figure(layout={'template':'plotly_dark'})

fig.add_trace(go.Surface(z=mresult[1], x=tx, y=ty))

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

fig.show()

# SIMILARIDAD COSENO

fig = go.Figure(layout={'template':'plotly_dark'})

fig.add_trace(go.Surface(z=result[0], x=tx, y=ty))

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

fig.show()

# ERROR NORMA

fig = go.Figure(layout={'template':'plotly_dark'})

fig.add_trace(go.Surface(z=result[1]-result[2], x=tx, y=ty))

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

fig.show()

# NORMA

fig = go.Figure(layout={'template':'plotly_dark'})

fig.add_trace(go.Surface(z=result[1], x=tx, y=ty))

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

fig.show()

# NORMA 2

fig = go.Figure(layout={'template':'plotly_dark'})

fig.add_trace(go.Surface(z=result[2], x=tx, y=ty))

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

fig.show()