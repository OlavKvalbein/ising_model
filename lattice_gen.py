import matplotlib.pyplot as plt
from lattice import Lattice

def spin_average(spin_2d):
    total = 0
    n = 0
    for row in spin_2d:
        total += sum(row)
        n += len(row)
    return total / n

gridsize = 100
temperature = 1.5

lattice_n = Lattice(gridsize, temperature)

MC_steps = 100  
m_hist = []

for step in range(MC_steps):
    for _ in range(gridsize**2):
        lattice_n.step()
    m_hist.append(spin_average(lattice_n.spin))

plt.figure()
plt.plot(m_hist)
plt.xlabel("MC step")
plt.ylabel("Spin average  m = <s>")
plt.show()

for _ in range(MC_steps*gridsize**2):
    lattice_n.step()
plt.imshow(lattice_n.spin, cmap="gray")
plt.show()