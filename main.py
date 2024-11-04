import imageio as io
import numpy as np

path = "x1.bmp"
input = io.read_image(path)
io.write_image("test.bmp", input)