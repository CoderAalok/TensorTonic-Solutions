import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    v = np.array(v)
    return np.diag(v)
    
    # matrix = np.zeros((v.size, v.size))
    # for i,val in enumerate(v):
    #     matrix[i,i] = val
    # return matrix
    
    