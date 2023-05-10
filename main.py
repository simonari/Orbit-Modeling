from datetime import datetime as dt
import numpy as np

import matplotlib.pyplot as plt

import os
import gc
import csv
import pandas as pd

from visibility.visibility import visibility

import satellites_orbits
from models import experiments

from tqdm import tqdm

def visibility_experiment():
    np.set_printoptions(precision=3, suppress=True)

    n = 10000
    cycle_number = 4

    print(f"[+] Output image resolution: {n}x{n} pixels.")
    visibility((n, n), cycle_number)


def eccentricity_experiment():
    periods = 3000
    chosen_orbit = satellites_orbits.orbits[0]
    chosen_eccentricity = 0.
    elements, t = experiments.eccentricity(chosen_orbit, chosen_eccentricity, periods)
    experiments.plot_elements(elements, chosen_eccentricity, periods, t)


def inclination_experiment():
    periods = 3000
    chosen_orbit = satellites_orbits.orbits[0]
    step = .1
    a, b = 56, 58

    with tqdm(total = int((b - a) / step)) as pbar:
        for inc_iter in np.arange(a, b, step):
            inc = np.deg2rad(inc_iter)
            elements, t = experiments.inclination(chosen_orbit, inc, periods)
            experiments.elements_to_csv(elements, periods)
            pbar.update(1)
            del elements
            gc.collect()
        # experiments.plot_elements(elements, inc, periods, t)


def analyze_files():
    dir = os.path.join(os.getcwd(), "data", "elements", "data", "nz-step-0.1")
    files = os.listdir(dir)

    deviations = []

    for file in files:
        # name = file.split("-")[1]
        df = pd.read_csv(os.path.join(dir, file))

        for val in df:
            df[val] -= df[val].values[0]
            df[val] = abs(df[val])

        deviations.append(df.describe().loc["max"].to_numpy())

    df = pd.DataFrame(deviations)
    fig, ax = plt.subplots()
    ax.plot(np.linspace(56, 58, len(deviations)), df[1], label="Эксцентриситет")
    ax.plot(np.linspace(56, 58, len(deviations)), df[2], label="Наклонение")
    ax.set_xticks(np.linspace(56, 58, 21))
    ax.legend(loc="upper center", ncol=2, frameon=False)
    ax.grid(True)
    plt.show()
    # 0.023962   0.012684
    # index_dev_min = np.argmin(deviations, axis=1)[:, [1, 2]]
    # print(index_dev_min)
    # print(deviations[index_dev_min, [1, 2]])

    # print(df.describe())


def plot_from_file(path):
    df = pd.read_csv(path)

    names = ["a", "e", "i", "O", "w"]
    titles = ["a", "e", "i", r"$\Omega$", r"$\omega$"]
    units = ["км", "", r"$\circ$", r"$\circ$", r"$\circ$"]

    n_periods = int(path.split("-")[-1].split(".")[0])
    t = df["a"].values.shape[0]
    print(t)
    n = 10
    time_scale = np.linspace(0, t, df["a"].values.shape[0])
    ticks = np.linspace(0, t, n + 1)
    labels = np.linspace(0, n_periods, n + 1, dtype=int)

    fig = plt.figure(figsize=(8, 6))
    ax_inc = fig.add_subplot(211)
    ax_inc.plot(time_scale, np.rad2deg(df["i"].values), label="i", c="black", lw=1)
    # ax_inc.plot(time_scale, np.rad2deg(df["i"].values - df.i.values[0]), label="i", c="black", lw=1)
    ax_inc.set_xticks(ticks)
    ax_inc.set_xticklabels(labels)
    ax_inc.grid(True)
    ax_inc.set_ylabel(r"Наклонение $i,\circ$")

    ax_e = fig.add_subplot(212, sharex=ax_inc)
    ax_e.plot(time_scale, df["e"].values, label="e", c="black", lw=1)
    # ax_e.plot(time_scale, df["e"].values - df.e.values[0], label="e", c="black", lw=1)
    # ax_e.set_xticks(ticks)
    # ax_e.set_xticklabels(labels)
    # ax_e.set_xticks([])
    # ax_e.set_xticklabels([])

    ax_e.grid(True)
    ax_e.set_ylabel(r"Эксцентрисистет $e$")
    plt.gcf()
    plt.subplots_adjust(hspace=0)

    # fig.suptitle("Элементы")
    # fig.suptitle("Возмущения в элементах")

    plt.show()

def main():
    time_start = dt.now()

    # eccentricity_experiment()
    # inclination_experiment()
    # analyze_files()
    plot_from_file("data/elements/data/nz-step-0.1/inc-57.60--p-3000.csv")

    print(f"[+] Exiting program.\n"
          f"[+] Execution took: {(dt.now() - time_start).total_seconds()}")


if __name__ == '__main__':
    main()
