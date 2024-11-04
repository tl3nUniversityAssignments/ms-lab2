import numpy as np

def multiply(*args):
    if len(args) == 0:
        return 0
    if len(args) == 1:
        return args[0]

    result = np.dot(args[0], args[1])
    for i in range(2, len(args)):
        result = np.dot(result, args[i])
    return result

def find_Z(A, inverse):
    E = np.identity(A.shape[1])
    return E - multiply(inverse, A)

def find_R(inverse):
    return multiply(inverse, inverse.T)