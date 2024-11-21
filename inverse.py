import numpy as np
from utils import *

def greville(matrix):
    # first step
    inverse = np.array(matrix)
    A0 = matrix[0]
    denominator = multiply(A0.T, A0)
    if (denominator == 0):
        inverse = np.vstack(A0)
    else:
        inverse = np.vstack(A0 / denominator)

    A = np.array([matrix[0]])
    n = matrix.shape[0]
    for i in range(1, n):
        a = matrix[i].reshape(-1, 1)
        Z = find_Z(A, inverse)
        A = np.vstack([A, matrix[i]]) # add row

        denominator = multiply(a.T, Z, a)[0, 0]
        if np.abs(denominator) == 0: #  or try eps < 0.001
            R = find_R(inverse)
            denominator = 1 + multiply(a.T, R, a)
            temp = inverse - multiply(R, a, a.T, inverse) / denominator
            inverse = np.hstack((temp, np.vstack((multiply(R, a) / denominator))))
        else:
            temp = inverse - multiply(Z, a, a.T, inverse) / denominator
            inverse = np.hstack((temp, np.vstack((multiply(Z, a) / denominator))))

    return inverse

def moore_penrose(A):
    delta = 10
    m = A.shape[0]
    n = A.shape[1]

    E = np.identity(n)
    if m < n:
        E = np.identity(m)
    
    previous = multiply(A.T, np.linalg.inv(multiply(A, A.T) + delta * E))
    while True:
        delta /= 2
        inverse = multiply(A.T, np.linalg.inv(multiply(A, A.T) + delta * E))
        if find_norm(previous, inverse) < 1e-10:
            return inverse
        else:
            previous = inverse
        

