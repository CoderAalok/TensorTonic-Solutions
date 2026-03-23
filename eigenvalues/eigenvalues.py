import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try:
        matrix = np.asarray(matrix, dtype=float)
        if matrix.size == 0 or matrix.ndim  < 2 or (matrix.shape[0] != matrix.shape[1]):
            return None
        res = np.linalg.eigvals(matrix)
        return res
    except ValueError:
        return None
