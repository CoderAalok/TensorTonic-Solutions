import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    a = np.array([x,y], dtype=float)
    res = np.sqrt(np.sum(np.diff(a, axis=0)**2))
    return res