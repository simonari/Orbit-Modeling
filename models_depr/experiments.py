import numpy as np
import csv

import satellites_orbits
from Classes.OrbitObjectPerturbed1 import OrbitObjectPerturbed1
from attractors import earth

from matplotlib import pyplot as plt


def plot_elements(elements, e, n_periods, t):
    names = ["a", "e", "i", "O", "w"]
    titles = ["a", "e", "i", r"$\Omega$", r"$\omega$"]
    units = ["км", "", r"$\circ$", r"$\circ$", r"$\circ$"]

    time_scale = np.linspace(0, t, len(elements[0]))

    n = 10
    ticks = np.linspace(0, t, n + 1)
    labels = np.linspace(0, n_periods, n + 1, dtype=int)

    fig = plt.figure(figsize=(10, 4))

    for i, elem in enumerate(elements):
        if i < 2:
            plt.plot(time_scale, elem, linewidth=1, c="black")
        else:
            plt.plot(time_scale, np.rad2deg(elem), linestyle="", marker=".", markersize=2.5, alpha=1, c="black")

        plt.xticks(ticks, labels=labels)

        plt.title(titles[i])
        plt.xlabel("Оборот")
        plt.ylabel(units[i])

        plt.grid(True)

        fig.savefig(f"data/elements/{names[i]}-e-{e:.2d}.p-{n_periods}.png")
        fig.clf()