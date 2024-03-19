import numpy as np

def spherical_vector(ndim=3):
    vec = np.random.randn(ndim)
    vec /= np.linalg.norm(vec, axis=-1)
    return vec

def linear_vector(ndim=3, inf_limit=-1, sup_limit=1):
    vec = np.random.uniform(inf_limit, sup_limit, (ndim,))
    return vec