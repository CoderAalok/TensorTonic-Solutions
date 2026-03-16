import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    dot_prod = np.dot(a,b)
    n1 = np.linalg.norm(a)
    n2 = np.linalg.norm(b)
    if n1 == 0 or n2 == 0:
        return 0
        
    return dot_prod/(n1*n2)