import numpy as np
import matplotlib.pyplot as plt

T = 5000
nWalkers = 10000
radius = 120


pos = []
for i in range(nWalkers):
    steps = np.random.choice([-1,1], T)
    pos.append(np.sum(steps))

pos = np.array(pos)
pos = (pos + radius) % (2*radius) - radius


mean = np.mean(pos)
meanOfSquared = np.mean(np.square(pos))

plt.title("Periodic randomwalk")
info = f"""
Timesteps = {T}, Walkers = {nWalkers}
Mean = {mean}, Mean of squares = {meanOfSquared}
radius = {radius}
"""
plt.subplots_adjust(bottom=0.2)
plt.figtext(0.5, 0.0, info, ha="center")
plt.hist(pos, 20)
plt.show()