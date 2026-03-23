import matplotlib.pyplot as plt
import numpy as np

from lattice import Lattice

gridsize = 16
ensemble_size = 
Ts = np.linspace(0.5, 4.0, 50)

steps = 1
burn_in_steps = 600
sample_steps = np.arange(burn_in_steps, steps, 10)

lattice = Lattice(gridsize)
spin_avg = []
for (i, T) in enumerate(Ts):
    lattice.T_J_ratio = T
    spin_avg_series = lattice.spin_avg_series(ensemble_size, steps, sample_steps)
    spin_avg.append(spin_avg_series.mean())
    print(f"\rTemperature {i+1} / {len(Ts)} done...", end="", flush=True)

plt.plot(Ts, spin_avg, "o")
plt.xlabel("Temperature $T$")
plt.ylabel("$|\\langle S \\rangle|$")
info = f"""$L$ = {gridsize},  periodic boundary,  ensemble size = {ensemble_size},  
MC steps = {steps},  burn in steps = {burn_in_steps}. """
plt.title(info)
plt.show()