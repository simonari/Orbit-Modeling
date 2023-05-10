from datetime import datetime as dt

import numpy as np

from matplotlib import pyplot as plt

import satellites_orbits
from Classes.OrbitObjectPerturbed1 import OrbitObjectPerturbed1
from attractors import earth

import warnings

def main():
    warnings.filterwarnings("ignore")
    plots()


def plots():
    time_start = dt.now()
    n_periods = 100

    orbit = satellites_orbits.satellite_ng1_s1
    orbit[1] = 0.
    sat = OrbitObjectPerturbed1(orbit, earth)

    t = n_periods * sat.T

    sol = sat.calculate_coordinates(n=n_periods)
    cs, vs = np.hsplit(sol.y.transpose(), 2)
    # x_p = np.linalg.norm(np.array(sat.x_p_arr), axis=1)

    k = 5
    elements = np.zeros((cs.shape[0], k))
    for i in range(cs.shape[0]):
        elements[i] = sat.rectangular_to_kepler(cs[i], vs[i])[:k]

    elements = np.hsplit(elements, k)

    n = 10
    ticks = np.linspace(0, t, n+1)
    labels = np.linspace(0, n_periods, n+1, dtype=int)

    fig = plt.figure()
    ax_a = fig.add_subplot(231)
    ax_e = fig.add_subplot(232)
    ax_i = fig.add_subplot(233)
    ax_w_lon = fig.add_subplot(234)
    ax_w_arg = fig.add_subplot(235)

    ax_a.set_title(f"a")
    ax_e.set_title(f"e")
    ax_i.set_title(f"i")
    ax_w_lon.set_title(r"$\Omega$")
    ax_w_arg.set_title(r"$\omega$")

    time_scale = np.linspace(0, t, cs.shape[0])

    ax_a.plot(time_scale, elements[0], linewidth=.5)
    ax_e.plot(time_scale, elements[1], linewidth=.5)
    ax_i.plot(time_scale, np.rad2deg(elements[2]), linewidth=.5)
    ax_w_lon.plot(time_scale, np.rad2deg(elements[3]), linewidth=.5, linestyle="", marker=".", markersize=2.5, alpha=1)
    ax_w_arg.plot(time_scale, np.rad2deg(elements[4]), linewidth=.5, linestyle="", marker=".", markersize=2.5, alpha=1)


    ax_a.set_xticks(ticks, labels=labels)
    ax_e.set_xticks(ticks, labels=labels)
    ax_i.set_xticks(ticks, labels=labels)
    ax_w_lon.set_xticks(ticks, labels=labels)
    ax_w_arg.set_xticks(ticks, labels=labels)

    print(f"[+] Exiting program.\n"
          f"[+] Execution took: {(dt.now() - time_start).total_seconds()}")

    plt.show()



if __name__ == '__main__':
    main()