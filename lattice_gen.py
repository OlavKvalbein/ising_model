import matplotlib.pyplot as plt
from lattice import Lattice

def spin_average(spin_2d):
    total = 0
    n = 0
    for row in spin_2d:
        total += sum(row)
        n += len(row)
    return total / n

gridsize = 64
T_values = [1.0, 1.5, 2.0, 2.5, 3.0]
T_values = [abs(T) for T in T_values]
MC_steps = 1000

N_sims = 10

m_hists = {}

for T in T_values:
    m_sum = [0.0] * MC_steps  

    for sim in range(N_sims):
        lattice_n = Lattice(gridsize, T)

        for step in range(MC_steps):
            print(
                f"\rT={T} | sim {sim+1}/{N_sims} | MC step {step+1}/{MC_steps}",
                end="",
                flush=True
            )

            lattice_n.MC_step()

            m_sum[step] += abs(spin_average(lattice_n.spin))
        print()

    m_hists[T] = [x / N_sims for x in m_sum]
    

plt.figure()
for T in T_values:
    plt.plot(m_hists[T], label=f"T={T}")

plt.xlabel("MC step")
plt.ylabel("Average |m| = average(|<s>|) over simulations")
plt.legend()
plt.show()


