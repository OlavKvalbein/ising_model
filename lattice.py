import matplotlib.pyplot as plt
import math
import random

class Lattice():
    def __init__(self, gridsize, temperature):
        self.size = gridsize
        self.T = temperature
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
            flip_probability = math.exp(-deltaE/self.T)
            if random.random() < flip_probability:
                self.spin[i][j] *= -1

    def MC_step(self):
        for _ in range(self.size**2):
            self.step()


if __name__ == "__main__":
    gridsize = 100
    temperature = 1.5
    lattice = Lattice(gridsize, temperature)
    MC_steps = 100
    for _ in range(MC_steps):
        lattice.MC_step()
    plt.imshow(lattice.spin, cmap="gray")
    plt.show()