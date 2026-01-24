import matplotlib.pyplot as plt
import math
import random

size = 100

T = 1.5 # temperature * boltzmann_k / epsilon

spin = [[0 for _ in range(size)] for _ in range(size)]

def initialize():
    for i in range(size):
        for j in range(size):
            spin[i][j] = random.choice([-1,1])
            # spin[i][j] = 1

def step():
    i = random.randint(0,size-1)
    j = random.randint(0,size-1)

    deltaE = energy_diff(i,j)
    if deltaE <= 0:
        spin[i][j] *= -1
    else:
        flip_probability = math.exp(-deltaE/T)
        if random.random() < flip_probability:
            spin[i][j] *= -1

def energy_diff(i, j):
    top = spin[(i-1)%size][j]
    bottom = spin[(i+1)%size][j]
    left = spin[i][(j-1)%size]
    right = spin[i][(j+1)%size]

    return 2*spin[i][j]*(top+bottom+left+right)


initialize()
for _ in range(100*size**2):
    step()
plt.imshow(spin, cmap="gray")
plt.show()