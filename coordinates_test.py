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
    n_periods = 3000

    orbit = satellites_orbits.satellite_ng1_s1
    orbit[1] = 0.
    # orbit[2] = np.deg2rad(64.8)
    sat = OrbitObjectPerturbed1(orbit, earth)

    t = n_periods * sat.T

    sol = sat.calculate_coordinates(n=n_periods)
    cs, vs = np.hsplit(sol.y.transpose(), 2)

    k = 5
    elements = np.zeros((cs.shape[0], k))
    for i in range(cs.shape[0]):
        elements[i] = sat.rectangular_to_kepler(cs[i], vs[i])[:k]

    elements = np.hsplit(elements, k)

    n = 10
    ticks = np.linspace(0, t, n+1)
    labels = np.linspace(0, n_periods, n+1, dtype=int)
    time_scale = np.linspace(0, t, cs.shape[0])

    names = ["a", "e", "i", "O", "w"]
    names_greek = ["a", "e", "i", r"$\Omega$", r"$\omega$"]
    units = ["км", "", r"$\circ$", r"$\circ$", r"$\circ$"]

    styles = {
        "a": {"c":"black", "lw":.75},
        "e": {"c":"black", "lw":.75},
        "i": {"c":"black", "lw":.75},
        "O": {"c":"black", "lw":.75, "ls":"", "marker":".", "ms":2.5, "alpha":1},
        "w": {"c":"black", "lw":.75, "ls":"", "marker":".", "ms":2.5, "alpha":1}
    }

    # plt.gcf()
    plt.rcParams["figure.figsize"] = (6.4, 4.8)
    plt.rcParams["axes.labelsize"] = 12

    if transparent:
        for k in styles:
            styles[k]["c"] = "white"
        plt.rcParams["text.color"] = "white"
        plt.rcParams["axes.labelcolor"] = "white"
        plt.rcParams["axes.edgecolor"] = "white"
        plt.rcParams["xtick.color"] = "white"
        plt.rcParams["ytick.color"] = "white"

    for i in range(len(names)):
        if i < 2:
            plt.plot(time_scale, elements[i], **styles[names[i]])
        else:
            plt.plot(time_scale, np.rad2deg(elements[i]), **styles[names[i]])

        plt.xticks(ticks, labels=labels)

        plt.xlabel("Обороты")
        plt.ylabel(f"{names_greek[i]}, {units[i]}" if units[i] != "" else f"{names_greek[i]}")

        plt.grid(True)
        plt.tight_layout()

        plt.savefig(f"data/current/{names[i]}.png", transparent=transparent)
        plt.clf()


    print(f"[+] Exiting program.\n"
          f"[+] Execution took: {(dt.now() - time_start).total_seconds()}")


if __name__ == '__main__':
    transparent = True
    main()