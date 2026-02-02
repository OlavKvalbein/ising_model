import numpy as np
import matplotlib.pyplot as plt

N = 10_000

def V(x):
    return x**4 - 2*x**2

def walker(delta, T):
    x = 0
    xs = [x]
    xi = np.random.random(N)*2 - 1  # random numbers in [-1, 1]
    step = xi * delta
    u = np.random.random(N) # random numbers in [0, 1]

    for i in range(N):
        x_new = x + step[i]
        deltaE = V(x_new) - V(x)
        if deltaE < 0:
            x = x_new
        else:
            probability = np.exp(-deltaE/T)
            if u[i] < probability:
                x = x_new
        xs.append(x)
    return xs

delta = 0.5
Ts = [0.1, 1.0, 10.0]
walks = [walker(delta, T) for T in Ts]

fig, ax = plt.subplots(nrows=1, ncols=len(Ts))
fig.suptitle("Particle in a well")

for i in range(len(Ts)):
    ax[i].hist(walks[i], bins=20)
    ax[i].set_xlim(-3, 3)
    ax[i].set_title(f"$T = {Ts[i]}$, $\delta$ = {delta}")

plt.show()