import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)
    
    dot_product = np.dot(a,b)
    norm1 = np.linalg.norm(a)
    norm2 = np.linalg.norm(b)
    if norm1 == 0 or norm2 == 0:
        return 0
    return dot_product/(norm1 * norm2)
    