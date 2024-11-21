import numpy as np
import imageio as io
import inverse
from utils import *

input = io.read_image('x1.bmp')
output = io.read_image('y9.bmp')

# calculate
X = np.array(input)
X = np.vstack((X, np.ones((1, X.shape[1]))))
Y = np.array(output)

X_inverse = inverse.moore_penrose(X)
#X_inverse = reverse.greville(X)

Z = np.identity(X.shape[0]) - multiply(X, X_inverse)
V = np.zeros((Y.shape[0], X.shape[0]))

A = multiply(Y, X_inverse) + multiply(V, Z)

# output
result = multiply(A, X)
io.write_image("result.bmp", result)

# test
print("Норма:", find_norm(result, Y))