import numpy as np
import matplotlib.pyplot as plt

def random_walk_1d(T, x0, prob=0.5):
    
    steps = np.random.choice([-1, 1], size=T, p=[1 - prob, prob])

    
    positions = np.empty(T + 1)
    positions[0] = x0
    positions[1:] = x0 + np.cumsum(steps)

    return positions

T = 50

positions = random_walk_1d(T,0)

plt.figure()
plt.plot(range(T + 1), positions)
plt.xlabel("t (timestep)")
plt.ylabel("x(t) (position)")
plt.title("1D Walk")
plt.grid(True)
plt.show()


def final_positions_random_walk(n_walkers, T, x0, prob=0.5):
    
    x0 = 0
    steps = np.random.choice([-1, 1], size=(n_walkers, T), p=[1 - prob, prob])

    # final position for each walker
    xT = x0 + steps.sum(axis=1)
    return xT

n_walkers = 1000
T = 200 

x_hist = final_positions_random_walk(n_walkers, T, 0)

bins = np.arange(x_hist.min() - 1.5, x_hist.max() + 1.5, 1)

plt.figure()
plt.hist(x_hist, bins=bins)
plt.xlabel("final position x(T)")
plt.ylabel("density")
plt.title(f"Histogram of final positions (N={n_walkers}, T={T})")
plt.grid(True)
plt.show()


#test