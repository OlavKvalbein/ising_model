import matplotlib.pyplot as plt
import numpy as np

from lattice import Lattice

gridsize = 16
MC_steps = 1000
sample_pts = np.arange(0, MC_steps, 10)
ensemble_size = 500
Ts = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5]

lattice = Lattice(gridsize, 0.0)

for i in range(len(Ts)):
    T = Ts[i]
    lattice.T_J_ratio = T
    spin_avg_series = lattice.spin_avg_series(ensemble_size, MC_steps, sample_pts)

    plt.plot(sample_pts, spin_avg_series, label=f"$T = {T}$")
    print(f"\rTemperature {i+1} / {len(Ts)} done...", end="", flush=True)

plt.xlabel("MC step")
plt.ylabel("$|<s>|$")
info = f"$L$ = {gridsize},  Periodic boundary,  Ensemble size = {ensemble_size}"
plt.figtext(0.5, 0.0, info, ha="center")
plt.legend()
plt.show()