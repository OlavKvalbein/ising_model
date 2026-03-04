import matplotlib.pyplot as plt
import numpy as np

class Lattice():
    def __init__(self, gridsize, temperature):
        self.size = gridsize
        self.T = temperature
        self.rng = np.random.default_rng()
        self.spin = self.rng.choice([-1,1], (self.size, self.size))

    # computes the energy difference from flipping the S_ij spin.
    # Periodic boundary conditions
    def energy_diff(self, i, j):
        top = self.spin[(i-1)%self.size, j]
        bottom = self.spin[(i+1)%self.size, j]
        left = self.spin[i, (j-1)%self.size]
        right = self.spin[i, (j+1)%self.size]

        return 2*self.spin[i, j]*(top+bottom+left+right)

    # does one attempt at flipping a spin
    def step(self):
        i, j = self.rng.integers(0,self.size,2)

        deltaE = self.energy_diff(i,j)
        if deltaE <= 0:
            self.spin[i, j] *= -1
        else:
            flip_probability = np.exp(-deltaE/self.T)
            if self.rng.random() < flip_probability:
                self.spin[i, j] *= -1

    # does gridsize^2 attempts at flipping a spin
    def MC_step(self):
        for _ in range(self.size**2):
            lattice.step()


if __name__ == "__main__":
    gridsize = 100
    temperature = 1.5
    lattice = Lattice(gridsize, temperature)
    MC_steps = 100
    for _ in range(MC_steps):
        lattice.MC_step()
    plt.imshow(lattice.spin, cmap="gray")
    plt.show()