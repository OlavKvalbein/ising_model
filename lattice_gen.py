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
T_values = [1.0, 1.5, 2.0, 2.5, 3.0]
T_values = [abs(T) for T in T_values]
MC_steps = 100


for temperature in T_values:
    lattice_n = Lattice(gridsize, temperature)
    m_hist = []

    for step in range(MC_steps):
        for _ in range(gridsize**2):
            lattice_n.step()
        m_hist.append(spin_average(lattice_n.spin))

    plt.plot(m_hist, label=f"T={temperature}")

plt.xlabel("MC step")
plt.ylabel("Spin average  m = <s>")
plt.legend()
plt.show()


fig, axes = plt.subplots(1, len(T_values), figsize=(8, 5))

for ax, T in zip(axes, T_values):
    lattice_n = Lattice(gridsize, T)

    for i in range(MC_steps):
        print(f"\rGenerating lattice series... MC step {i+1}/{MC_steps}", end="", flush=True)

        for _ in range(gridsize**2):
            lattice_n.step()
    print()
    ax.imshow(lattice_n.spin, cmap="gray")
    ax.axis("off")
    ax.set_title(f"T = {T}")
    
    

plt.tight_layout()
plt.show()

