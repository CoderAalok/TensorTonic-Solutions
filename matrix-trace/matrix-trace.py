import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A = np.array(A, dtype=float)
    A_shape = A.shape
    if A_shape[0] != A_shape[1] or A.ndim > 2:
        return None
        
    dia_sum = 0
    for i in range(A_shape[0]):
        dia_sum += A[i,i]

    return int(dia_sum)
    
    
    
    
