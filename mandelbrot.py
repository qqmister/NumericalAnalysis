import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if (abs(z) > 2):
            return n
        z = z**2 + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    mset = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            c = complex(x[j], y[i])
            mset[i, j] = mandelbrot(c, max_iter)

    return mset

xmin, xmax, ymin, ymax = -2.0, 1.5, -1.5, 1.5
width, height = 1000, 1000
max_iter = 1000

mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

plt.imshow(mandelbrot_image, extent=[xmin, xmax, ymin, ymax], cmap='hot')
plt.colorbar()
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()

                       