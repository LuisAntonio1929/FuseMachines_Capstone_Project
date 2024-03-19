import numpy as np

def w_2_so3(w):
  w1 = w[0]
  w2 = w[1]
  w3 = w[2]
  wt = np.array([[0, -w3, w2],
                 [w3, 0, -w1],
                 [-w2, w1, 0]])
  return wt

def so3_2_w(w):
  return np.array([w[-1,1],w[0,-1],w[1,0]])

def t_2_se3(s):
  M = np.zeros((4,4))
  M[:3,:3] = w_2_so3(s[:3])
  M[:3,-1] = s[3:]
  return M

def se3_2_t(s):
  w_hat = s[:3,:3]
  v = s[:3,-1]
  return np.concatenate((so3_2_w(w_hat),v))

def R(w_hat,theta):
  return np.eye(3) + np.sin(theta)*w_hat + (1-np.cos(theta))*w_hat@w_hat

def p(w_hat,theta,v):
  R_int = np.eye(3)*theta + (1-np.cos(theta))*w_hat + (theta-np.sin(theta))*w_hat@w_hat
  return R_int@v

def G(w_hat,theta):
  G = np.eye(3)/theta - 0.5*w_hat + (1/theta - 0.5/np.tan(theta/2))*w_hat@w_hat
  return G

def w_2_SO3(w,theta):
  return R(w_2_so3(w),theta)

def SO3_2_w(R):
  if np.trace(R)+1<=1e-10:
    theta = np.pi
    w = (1/(2*(1+R[0,0])**.5))*np.array([1+R[0,0],R[1,0],R[2,0]])
  else:
    theta = np.arccos(0.5*(np.trace(R)-1))
    w = so3_2_w((1/(2*np.sin(theta)))*(R-R.T))
  return w,theta

def SE3_2_t(TH):
  w,theta = SO3_2_w(TH[:3,:3])
  w_hat = w_2_so3(w)
  v = G(w_hat,theta)@TH[:3,-1]
  return np.concatenate((w,v)), theta

def t_2_SE3(t,theta):
  w = t[:3]
  v = t[3:]
  w_hat = w_2_so3(w)
  Ri = R(w_hat,theta)
  pi = p(w_hat,theta,v)
  TH = np.eye(4)
  TH[:3,:3] = Ri
  TH[:-1,-1] = pi
  return TH

def cr_param(M):
    return -(np.eye(3) - M)@np.linalg.inv(np.eye(3) + M)

def ct_param(M):
    return -(np.eye(4) - M)@np.linalg.inv(np.eye(4) + M)

def lie_bracket_t(A,B):
  A = t_2_se3(A)
  B = t_2_se3(B)
  lb = A@B-B@A
  return se3_2_t(lb)

