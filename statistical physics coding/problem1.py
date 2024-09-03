import numpy as np
import matplotlib.pyplot as plt

def initialize(size):
    """Initialize the spin lattice randomly."""
    return np.random.choice([-1, 1], size=(size, size))

def deltaU(s, i, j, size):
    """Compute the change in energy if the spin at (i, j) is flipped."""
    top = s[(i-1) % size, j]
    bottom = s[(i+1) % size, j]
    left = s[i, (j-1) % size]
    right = s[i, (j+1) % size]
    return 2 * s[i, j] * (top + bottom + left + right)

def colorsquare(ax, s, size):
    """Update the plot with the current state of the lattice."""
    ax.clear()
    ax.imshow(s, cmap='bwr', interpolation='nearest')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f'Size: {size}')
    plt.pause(0.001)

def ising_model(size, T, iterations):
    s = initialize(size)
    fig, ax = plt.subplots()
    for _ in range(iterations):
        i = np.random.randint(size)
        j = np.random.randint(size)
        Ediff = deltaU(s, i, j, size)
        if Ediff <= 0 or np.random.rand() < np.exp(-Ediff / T):
            s[i, j] = -s[i, j]
        colorsquare(ax, s, size)
    plt.show()

if __name__ == "__main__":
    size = int(input("Size of lattice (max 50): "))
    T = float(input("Temperature (units of epsilon/k): "))
    iterations = 100 * size ** 2
    ising_model(size, T, iterations)