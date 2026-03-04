import matplotlib.pyplot as plt

import math
import random

class Lattice():
    def __init__(self, gridsize, T_J_ratio):
        self.size = gridsize
        self.T_J_ratio = T_J_ratio
        self.spin = [[random.choice([-1,1]) for _ in range(self.size)] for _ in range(self.size)]

    def energy_diff(self, i, j):
        top = self.spin[(i-1)%self.size][j]
        bottom = self.spin[(i+1)%self.size][j]
        left = self.spin[i][(j-1)%self.size]
        right = self.spin[i][(j+1)%self.size]

        return 2*self.spin[i][j]*(top+bottom+left+right)
    
    def step(self):
        i = random.randint(0,self.size-1)
        j = random.randint(0,self.size-1)

        deltaE = self.energy_diff(i,j)
        if deltaE <= 0:
            self.spin[i][j] *= -1
        else:
            flip_probability = math.exp(-deltaE/self.T_J_ratio)
            if random.random() < flip_probability:
                self.spin[i][j] *= -1

    def MC_step(self):
        for _ in range(self.size**2):
            self.step()


if __name__ == "__main__":
    gridsize = 300
    T_J_ratio = 1.5
    lattice = Lattice(gridsize, T_J_ratio)
    MC_steps = 100
    for i in range(MC_steps):
        print(f"\rGenerating lattice series... MC step {i+1}/{MC_steps}", end="", flush=True)
        lattice.MC_step()
    plt.imshow(lattice.spin, cmap="gray")
    plt.show()