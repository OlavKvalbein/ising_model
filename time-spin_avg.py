import matplotlib.pyplot as plt
import numpy as np

from lattice import Lattice

gridsize = 16
steps = 500 # MC steps
sample_steps = np.arange(0, steps, 10)
ensemble_size = 100
Ts = [0.5,1.0,1.5,2.0,2.5,3.0]

lattice = Lattice(gridsize, 0.0)

for i in range(len(Ts)):
    T = Ts[i]
    lattice.T_J_ratio = T
    spin_avg_series = lattice.spin_avg_series(ensemble_size, steps, sample_steps)

    plt.plot(sample_steps, spin_avg_series, label=f"$T = {T}$")
    print(f"\rTemperature {i+1} / {len(Ts)} done...", end="", flush=True)

plt.xlabel("MC step")
plt.ylabel("$|<s>|$")
info = f"$L$ = {gridsize},  Periodic boundary,  Ensemble size = {ensemble_size}"
plt.figtext(0.5, 0.0, info, ha="center")
plt.legend()
plt.show()