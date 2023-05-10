import numpy as np
import csv

import satellites_orbits
from Classes.OrbitObjectPerturbed1 import OrbitObjectPerturbed1
from attractors import earth

from matplotlib import pyplot as plt


def eccentricity(orbit, e=0.0, n_periods=1):
    orbit = orbit.copy()
    orbit[1] = e

    sat = OrbitObjectPerturbed1(orbit, earth)

    t = n_periods * sat.T

    sol = sat.calculate_coordinates(n=n_periods)
    cs, vs = np.hsplit(sol.y.transpose(), 2)

    k = 5
    elements = np.zeros((cs.shape[0], k))
    for i in range(cs.shape[0]):
        elements[i] = sat.rectangular_to_kepler(cs[i], vs[i])[:k]

    # x_p = np.linalg.norm(np.array(sat.x_p_arr), axis=1)
    # a_ratio = np.array([x_p[i] / elements[i, 0] for i in range(cs.shape[0])])

    return np.hsplit(elements, k), t


def inclination(orbit, inc, n_periods=1):
    orbit = orbit.copy()
    orbit[2] = inc

    sat = OrbitObjectPerturbed1(orbit, earth)

    t = n_periods * sat.T

    sol = sat.calculate_coordinates(n=n_periods)
    cs, vs = np.hsplit(sol.y.transpose(), 2)

    k = 5
    elements = np.zeros((cs.shape[0], k))
    for i in range(cs.shape[0]):
        elements[i] = sat.rectangular_to_kepler(cs[i], vs[i])[:k]

    # x_p = np.linalg.norm(np.array(sat.x_p_arr), axis=1)
    # a_ratio = np.array([x_p[i] / elements[i, 0] for i in range(cs.shape[0])])
    del sol, cs, vs, sat
    return np.hsplit(elements, k), t


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

def elements_to_csv(elements, n_periods):
    # print(elements)
    inc = elements[2][0, 0]
    with open(f"data/elements/data/nz-step-0.1/inc-{np.rad2deg(inc):.2f}--p-{n_periods}.csv", "w", newline="") as file:
        header = ["a", "e", "i", "O", "w"]

        writer = csv.writer(file)
        writer.writerow(header)

        for i in range(elements[0].shape[0]):
            row = []
            for elem in elements:
                row.append(elem[i, 0])
            writer.writerow(row)
    # print(f"Saved to data/elements/data/inc-{np.rad2deg(inc):.2f}--p-{n_periods}.csv\n")