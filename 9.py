import numpy as np
import matplotlib.pyplot as plt

def EscVel(z, c, N):
    for n in range(N):
        if (abs(z) > 2): #check if it escaped 
            return n #return the iter number when it escaped
        z = z**2 + c #mandelbrot formula
    return N #if it never escape, return max iter

def JuliaSet(zMax, c, N):
    size = 500 #grid resolution
    x = np.linspace(-zMax, zMax, size) # real part grid
    y = np.linspace(-zMax, zMax, size) # imaginary part grid
    mset = np.zeros((size, size)) #escape time matrix
    
    X, Y = np.meshgrid(x, y) #full 2d grid
    Z0 = X + 1j * Y  # convert into complex numbers

    for i in range(size):
        for j in range(size):
            z = Z0[i, j]  # Get the correct complex number
            mset[i, j] = EscVel(z, c, N)


    return mset

N = 100
c_values = [
    complex(-.297491, 0.641051),
    complex(-.79, .15),
    complex(-.162, 1.04),
    complex(.3, -.01),
    complex(-1.476, 0),
    complex(-.12, -.77), #intriticate set, requires higher N
    complex(0.28, .008),
    complex(0, 0.8) #bonus plot
]
#dictionary for dynamic zMax values
zMaxD = {
    complex(-.79, .15): 0.9,
    complex(-.162, 1.04): 0.3,
    complex(-1.476, 0) : 0.65,
    complex(-.12, -.77) : 0.8,
    complex(0, 0.8) : 1.6
}
#dynamic N
N_dict = {
    complex(-.12, -.77) : 300
}


# Create a figure with multiple subplots (3 rows, 3 columns)
fig, axes = plt.subplots(2, 4, figsize=(15, 8))  # Adjust rows/columns as needed
axes = axes.ravel()  # Flatten axes for easy iteration

# Generate and plot each Julia set
for i, c in enumerate(c_values):
    zMax = zMaxD.get(c, 1.2)  
    N = N_dict.get(c, 100)

    M = JuliaSet(zMax, c, N)  # Compute the Julia Set
    axes[i].imshow(np.arctan(0.1 * M), extent=[-zMax, zMax, -zMax, zMax], cmap='inferno', origin='lower')
    axes[i].set_title(f"c = {c}")
    axes[i].set_xlabel("Real Axis")
    axes[i].set_ylabel("Imaginary Axis")

# Adjust layout to fit all subplots nicely
plt.tight_layout()
plt.show()