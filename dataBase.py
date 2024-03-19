import numpy as np
from vectors import *
from transformations import *
import pandas as pd

npoints = 100000 #numero de puntos
ndim = 3 #numero de dimensiones

def data_gen():
  #vectores de rotacion (screws)
  w1 = spherical_vector(ndim)
  w2 = spherical_vector(ndim)

  #puntos de aplicacion del screw
  q1 = linear_vector(ndim)
  q2 = linear_vector(ndim)

  #expresion en se3 para velocidad lineal en rotacion pura
  v1 = np.cross(-w1,q1)
  v2 = np.cross(-w2,q2)

  theta1 = linear_vector(1, -np.pi, np.pi)
  theta2 = linear_vector(1, -np.pi, np.pi)

  #vector R6 de se3
  wv1 = np.concatenate((w1,v1))
  wv2 = np.concatenate((w2,v2))

  #primeros 6 componentes de Baker–Campbell–Hausdorff formula
  r1 = wv1*theta1/np.pi
  r2 = wv2*theta2/np.pi
  r12 = lie_bracket_t(r1,r2)
  r112 = lie_bracket_t(r1,r12)
  r221 = lie_bracket_t(r2,-r12)
  r2112 = lie_bracket_t(r2,r112)

  #producto escalar
  dr1r2 = np.dot(r1[:3],r2[:3])

  #composicion de transformaciones
  TH1 = t_2_SE3(wv1,theta1)
  TH2 = t_2_SE3(wv2,theta2)
  TH3 = TH1@TH2
  wv3,theta3 = SE3_2_t(TH3)

  r3 = wv3*theta3/np.pi

  #calculo de coeficientes Ax=b
  #matriz A
  A = np.vstack((r1,r2,r12,r112,r221,r2112)).T

  #coeficientes "x"
  c = np.linalg.pinv(A) @ r3

  return np.concatenate((r1,r2,r12,r112,r221,r2112,[dr1r2],theta1,theta2,c,r3,[theta3]))

data = np.array([data_gen() for _ in range(npoints)])

c = data[:,-13:-7]
dr1r2 =  data[:,-16]
theta1 = data[:,-15]/np.pi
theta2 = data[:,-14]/np.pi
dv1v2 = np.sum(data[:,3:6]*data[:,9:12], axis=1)
dw1v2 = np.sum(data[:,0:3]*data[:,9:12], axis=1)
dw2v1 = np.sum(data[:,6:9]*data[:,3:6], axis=1)

df = pd.DataFrame({'c1':c[:,0],'c2':c[:,1],'c3':c[:,2],'c4':c[:,3],'c5':c[:,4],'c6':c[:,5],'dr1r2':dr1r2,'theta1':theta1,'theta2':theta2,'dv1v2':dv1v2,'dw1v2':dw1v2,'dw2v1':dw2v1})

df.to_excel("data.xlsx")