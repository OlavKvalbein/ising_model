import numpy as np
import matplotlib.pyplot as plt

T = 500
nWalkers = 10000

pos = []
for i in range(nWalkers):
    steps = np.random.choice([-1,1], T)
    pos.append(np.sum(steps))

mean = np.mean(pos)
meanOfSquares = np.mean(np.square(pos))

info = f"""
Timesteps = {T}, Walkers = {nWalkers}
Mean = {mean}, Mean of squares = {meanOfSquares}
"""
plt.title("Randomwalk")
plt.subplots_adjust(bottom=0.2)
plt.figtext(0.5, 0.0, info, ha="center")
plt.hist(pos, 20)
plt.show()