from lattice import Lattice
import matplotlib.pyplot as plt

gridsize = 100
temperature = 0.5
lattice = Lattice(gridsize, temperature)
MC_steps = 100
for _ in range(MC_steps*gridsize**2):
    lattice.step()
plt.imshow(lattice.spin, cmap="gray")
plt.show()