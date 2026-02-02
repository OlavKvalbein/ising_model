import numpy as np
import matplotlib.pyplot as plt

N = 10_000
def walker(delta):
    x = 0
    xs = [x]
    xi = np.random.random(N)*2 - 1  # random numbers between -1 and 1
    step = xi * delta
    u = np.random.random(N)

    for i in range(N):
        x_new = x + step[i]
        alpha = np.exp((x**2 - x_new**2)/2)
        if u[i] < alpha:
            x = x_new
        xs.append(x)
    return xs

t = [i for i in range(N+1)]
deltas = [0.001, 0.01, 0.1, 1.0]
walks = [walker(delta) for delta in deltas]

fig, ax = plt.subplots(nrows=1, ncols=len(deltas))
fig.suptitle("Gaussian walks")

for i in range(len(deltas)):
    ax[i].plot(t, walks[i])
    ax[i].set_ylim(-3, 3)
    ax[i].set_title(f"$\delta$ = {deltas[i]}")

plt.show()