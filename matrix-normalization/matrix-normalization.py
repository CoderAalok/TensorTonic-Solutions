import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here
    matrix = np.array(matrix, dtype=float)
    # edge case
    if matrix.size == 0 or (axis is not None and (axis >= matrix.ndim or 
    axis < -matrix.ndim)) or matrix.ndim > 2:
        return None
    # for norm type -> l1
    if norm_type == 'l1':
        norm = np.sum(np.abs(matrix), axis=axis, keepdims=True)

    # for norm type -> l2
    elif norm_type == 'l2':
        norm = np.sqrt(np.sum(matrix**2, axis=axis, keepdims=True))

     # for norm type -> max
    elif norm_type == 'max':
        norm = np.max(np.abs(matrix), axis=axis, keepdims=True)

    else:
        return None

    norm[norm==0] = 1 # zero division handling

    return matrix / norm
