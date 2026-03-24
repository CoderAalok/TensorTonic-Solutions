import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    
    # res = np.sqrt(np.sum(np.diff(a, axis=0)**2))
    res = np.linalg.norm(x-y)
    return res