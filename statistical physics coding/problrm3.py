import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def initialize(size):
    """Initialize the 3D spin lattice randomly."""
    s = np.random.choice([-1, 1], size=(size, size, size))
    return s


def deltaU(s, i, j, k, size):
    """Compute the change in energy if the spin at (i, j, k) is flipped."""
    top = s[(i - 1) % size, j, k]
    bottom = s[(i + 1) % size, j, k]
    left = s[i, (j - 1) % size, k]
    right = s[i, (j + 1) % size, k]
    front = s[i, j, (k - 1) % size]
    back = s[i, j, (k + 1) % size]
    return 2 * s[i, j, k] * (top + bottom + left + right + front + back)


def colorsquare(ax, s, i, j, k, size):
    """Draw the frontmost panel of the 3D lattice."""
    if k != 0:
        return
    color = 'red' if s == 1 else 'yellow'
    rect = plt.Rectangle((j, i), 1, 1, facecolor=color, edgecolor='black')
    ax.add_patch(rect)


def ising_model(size, T):
    s = initialize(size)

    fig, ax = plt.subplots()
    ax.set_xlim(0, size)
    ax.set_ylim(0, size)

    while True:
        for _ in range(100):
            i = np.random.randint(size)
            j = np.random.randint(size)
            k = np.random.randint(size)
            Ediff = deltaU(s, i, j, k, size)
            if Ediff <= 0 or np.random.rand() < np.exp(-Ediff / T):
                s[i, j, k] = -s[i, j, k]
                colorsquare(ax, s[i, j, k], i, j, k, size)

        plt.draw()
        plt.pause(0.01)
        if plt.waitforbuttonpress(timeout=0.1):
            break

    plt.show()


if __name__ == "__main__":
    size = int(input("Lattice size (max 20): "))
    T = float(input("Temperature (units of epsilon/k): "))
    ising_model(size, T)