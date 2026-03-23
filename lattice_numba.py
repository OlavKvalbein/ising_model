import matplotlib.pyplot as plt
import numpy as np

import math

from numba import int32, float64, njit
from numba.experimental import jitclass

spec = [
    ("size", int32),
    ("T_J_ratio", float64),
    ("spin", int32[:, :])
]

@jitclass(spec)
class Lattice():
    def __init__(self, gridsize, T_J_ratio, rng):
        self.size = gridsize
        self.T_J_ratio = T_J_ratio
        self.spin = np.zeros((self.size, self.size), dtype=np.int32)
        reset_spin(self, rng)

@njit
def reset_spin(lat, rng):
    lat.spin = rng.integers(0, 2, size=(lat.size, lat.size), dtype=np.int32)
    lat.spin = lat.spin * 2 - 1

@njit
def energy_diff(lat, i, j):
    top = lat.spin[(i-1)%lat.size,j]
    bottom = lat.spin[(i+1)%lat.size,j]
    left = lat.spin[i,(j-1)%lat.size]
    right = lat.spin[i,(j+1)%lat.size]

    return 2*lat.spin[i,j]*(top+bottom+left+right)

@njit
def step(lat, rng):
    i, j = rng.integers(0, lat.size-1, 2)

    deltaE = energy_diff(lat, i, j)
    if deltaE <= 0:
        lat.spin[i,j] *= -1
    else:
        flip_probability = math.exp(-deltaE/lat.T_J_ratio)
        if rng.random() < flip_probability:
            lat.spin[i,j] *= -1

@njit
def MC_step(lat, rng):
    for _ in range(lat.size**2):
        step(lat, rng)

@njit
def spin_avg(lat):
    return abs(lat.spin.sum() / lat.size**2)

# the absolute average spin as a timeseries, averaged over an ensemble
@njit
def spin_avg_series(lat, ensemble_size, MC_steps, sample_pts, rng):
    # sum of the spin averages over an ensemble as a timeseries
    ensemble_sum = np.zeros(len(sample_pts))
    
    # looping over each instance in the ensemble
    for _ in range(ensemble_size):
        # resetting the lattice for a new instance
        reset_spin(lat)

        # adding to the ensemble sum
        ensemble_sum[0] += abs(spin_avg(lat))
        for sample_nr in range(1, len(sample_pts)):
            # how many MC steps between each sample
            MC_steps = sample_pts[sample_nr] - sample_pts[sample_nr-1]

            for _ in range(MC_steps):
                MC_step(lat)
            
            abs_spin_avg = spin_avg(lat)
            ensemble_sum[sample_nr] += abs_spin_avg
    
    return ensemble_sum / ensemble_size

if __name__ == "__main__":
    gridsize = 32
    T_J_ratio = 1.5
    rng = np.random.default_rng()
    lattice = Lattice(gridsize, T_J_ratio, rng)
    MC_steps = 100
    for i in range(MC_steps):
        print(f"\rGenerating lattice series... MC step {i+1}/{MC_steps}", end="", flush=True)
        MC_step(lattice)
    plt.imshow(lattice.spin, cmap="gray")
    plt.show()