import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    # [[2,3],
    #  [4,5]]

    X = np.asarray(X)
    # Total data
    N = X.shape[0]

    if N < 2  or X.ndim < 2:
        return None
    
    # Step 1: center the data
    mu = np.mean(X, axis=0)
    X_centered = X - mu

    # Step 2: Compute Covariance Matrix
    summation = (1/(N-1)) * (X_centered.T @ X_centered)

    # result
    return summation
    
    