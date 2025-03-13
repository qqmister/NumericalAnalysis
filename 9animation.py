import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Escape Velocity Function
def EscVel(z, c, N):
    for n in range(N):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return N

# Julia Set Function
def JuliaSet(zMax, c, N, size=500):
    x = np.linspace(-zMax, zMax, size)
    y = np.linspace(-zMax, zMax, size)
    X, Y = np.meshgrid(x, y)
    Z0 = X + 1j * Y  # Create grid of complex numbers
    
    M = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            z = Z0[i, j]
            M[i, j] = EscVel(z, c, N)
    
    return M

# Set up animation parameters
c = complex(-0.79, 0.15)  # Julia set parameter
N = 100                   # Max iterations
size = 500                # Grid size
zMax_values = np.linspace(2, 0.5, 100)  # Zooming in from zMax=2 to zMax=0.5

# Create figure
fig, ax = plt.subplots()

# Initialize first frame
M = JuliaSet(zMax_values[0], c, N)
im = ax.imshow(np.arctan(0.1 * M), extent=[-zMax_values[0], zMax_values[0], -zMax_values[0], zMax_values[0]], cmap='inferno', origin='lower')

# Animation update function
def update(frame):
    zMax = zMax_values[frame]
    M = JuliaSet(zMax, c, N)
    im.set_data(np.arctan(0.1 * M))
    im.set_extent([-zMax, zMax, -zMax, zMax])
    ax.set_title(f"zMax = {zMax:.2f}")

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(zMax_values), interval=50)

# Show animation
plt.show()
