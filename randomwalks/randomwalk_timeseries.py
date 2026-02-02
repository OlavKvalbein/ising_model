import numpy as np
import matplotlib.pyplot as plt

T = 5000
nWalkers = 10000

pos = np.array([0 for _ in range(nWalkers)])
means = []
for i in range(T):
    step = np.random.choice([-1,1], nWalkers)
    pos += step
    means.append(np.mean(pos))

meanOfSquares = np.mean(np.square(pos))

info = f"""
Timesteps = {T}, Walkers = {nWalkers}
Mean = {means[-1]}, Mean of squares = {meanOfSquares}
"""


plt.title("Randomwalk")
plt.subplots_adjust(bottom=0.2)
plt.figtext(0.5, 0.0, info, ha="center")
# plt.hist(pos, 20)
plt.plot(means, [i+1 for i in range(T)])
plt.ylabel("time")
plt.xlabel("mean displacement")
plt.show()