import numpy as np
import matplotlib.pyplot as plt

def EscVel(z, c, N):
    for i in range(N):
        if abs(z) > 2:
            return i
        z = z**2 + c
    return N

def JuliaSet(zMax, c, N):
    size = 500
    x = np.linspace(-zMax, zMax)
    y = np.linspace(-zMax, zMax)
    mset = np.zeros((size, size))

    X, Y = np.meshgrid(x, y)
    Z0 = X + 1j * Y 

    for i in range(x):
        for j in range(y):
            z = Z0[i, j]
            mset[i, j] = EscVel(z, c, N)

        return mset