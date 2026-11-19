import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    rows = len(A)
    cols = len(A[0])
    
    # Initialize an empty M x N array
    result = np.empty((cols, rows), dtype=type(A[0][0]))
    
    for i in range(rows):
        for j in range(cols):
            result[j, i] = A[i][j]
            
    return result