import matplotlib.pyplot as plt
import numpy as np

from lattice import Lattice

# def spin_average_series(gridsize, T, MC_steps, sample_freq):
#     lattice = Lattice(gridsize, T)
#     spin_average = []
#     for i in range(MC_steps):
#         if i % sample_freq == 0:
#             m = abs(lattice.spin_average())
#             spin_average.append(m)

#         lattice.MC_step()
#     return spin_average



# def ensemble_average_series(count, gridsize, T, MC_steps, sample_freq):
#     ensemble_sum = np.array(spin_average_series(gridsize, T, MC_steps, sample_freq))
#     for _ in range(count-1):
#         series = np.array(spin_average_series(gridsize, T, MC_steps, sample_freq))
#         ensemble_sum += series
#     return ensemble_sum / count


# import timeit
# n = 10
# total_time = timeit.timeit(lambda: spin_average_series(16, 2.0, 1000, 10), number=n)
# average = total_time / n
# print(average)



if __name__=="__main__":
    gridsize = 16
    MC_steps = 1000
    sample_pts = np.arange(0, MC_steps, 10)
    ensemble_size = 500
    Ts = [2.0, 2.5, 3.0]

    lattice = Lattice(gridsize, 0.0)

    for i in range(len(Ts)):
        T = Ts[i]
        lattice.T_J_ratio = T
        spin_avg_series = lattice.spin_avg_series(ensemble_size, MC_steps, sample_pts)

        plt.plot(sample_pts, spin_avg_series, label=f"$T = {T}$")
        print(f"\rTemperature {i+1} / {len(Ts)} done", end="", flush=True)

    plt.xlabel("MC step")
    plt.ylabel("$|<s>|$")
    info = f"$S = {gridsize}, MC steps = {MC_steps}, Ensemble size = {ensemble_size}$"
    plt.figtext(0.5, 0.0, info, ha="center")
    plt.legend()
    plt.show()