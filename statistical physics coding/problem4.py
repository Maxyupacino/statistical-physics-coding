import numpy as np
import matplotlib.pyplot as plt


def initialize(size):
    """Initialize the spin lattice randomly."""
    return np.random.choice([-1, 1], size=(size, size))


def deltaU(s, i, j, size):
    """Compute the change in energy if the spin at (i, j) is flipped."""
    top = s[(i - 1) % size, j]
    bottom = s[(i + 1) % size, j]
    left = s[i, (j - 1) % size]
    right = s[i, (j + 1) % size]
    return 2 * s[i, j] * (top + bottom + left + right)


def bst(s, size):
    """Perform the block spin transformation."""
    new_size = size // 3
    transformed = np.zeros((new_size, new_size))
    for i in range(1, size - 1, 3):
        for j in range(1, size - 1, 3):
            block_sum = np.sum(s[i - 1:i + 2, j - 1:j + 2])
            transformed[i // 3, j // 3] = np.sign(block_sum)
    return transformed


def plot_lattice(ax, s, size):
    """Plot the lattice."""
    ax.clear()
    ax.imshow(s, cmap='coolwarm', interpolation='nearest')
    ax.set_xticks(np.arange(-0.5, size, 1))
    ax.set_yticks(np.arange(-0.5, size, 1))
    ax.grid(color='k', linestyle='-', linewidth=1)


def ising_model(size, T):
    s = initialize(size)

    fig, ax = plt.subplots()
    ax.set_xlim(-0.5, size - 0.5)
    ax.set_ylim(-0.5, size - 0.5)

    while True:
        for _ in range(10000):
            i, j = np.random.randint(size), np.random.randint(size)
            Ediff = deltaU(s, i, j, size)
            if Ediff <= 0 or np.random.rand() < np.exp(-Ediff / T):
                s[i, j] = -s[i, j]

        s_transformed = bst(s, size)
        plot_lattice(ax, s_transformed, size // 3)
        plt.draw()
        plt.pause(0.01)

        if plt.waitforbuttonpress(timeout=0.1):
            break

    plt.show()


if __name__ == "__main__":
    size = int(input("Lattice size (max 120): "))
    size -= size % 3  # Ensure the size is divisible by 3
    T = float(input("Temperature (units of epsilon/k): "))
    ising_model(size, T)