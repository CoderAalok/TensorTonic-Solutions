import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    A = np.array(A, dtype=float)
    # edge case 
    if A.shape[0] != A.shape[1] or A.ndim > 2 or np.linalg.det(A) == 0:
        return None

    A_inv = np.linalg.inv(A)
    I = A@A_inv
    res = np.linalg.norm((A@A_inv - I))
    return A_inv
    
    