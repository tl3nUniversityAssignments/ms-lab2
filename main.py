import numpy as np
import imageio as io
import reverse

"""
IO
path = "x1.bmp"
input = io.read_image(path)
io.write_image("test.bmp", input)
"""

"""
Greville
test = np.array([[1, 1], [0, 0]])
print(reverse.greville(test))
"""

"""
Moore-Penrose
"""
test = np.array([[1, 1], [0, 0]])
print(reverse.moore_penrose(test))
