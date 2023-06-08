from datetime import datetime as dt
import numpy as np

import matplotlib.pyplot as plt

import os
import pandas as pd
import sys

from visibility.visibility import visibility

import variations

from tqdm import tqdm
import plotter
import parser
import models
import analyzer
import scipy

def visibility_experiment():
    np.set_printoptions(precision=3, suppress=True)

    n = 100
    cycle_number = 6

    print(f"[+] Output image resolution: {n}x{n} pixels.")
    visibility((n, n), cycle_number)


def analyze_files():
    directory = os.path.join(os.getcwd(), "data", "elements", "data", "nz-step-0.1")
    files = os.listdir(directory)

    deviations = []

    for file in files:
        # name = file.split("-")[1]
        df = pd.read_csv(os.path.join(directory, file))

        for val in df:
            df[val] -= df[val].values[0]
            df[val] = abs(df[val])

        deviations.append(df.describe().loc["max"].to_numpy())

    # plt.rcParams["ytick.left"] = False
    plt.rcParams["ytick.labelleft"] = False

    transparent = True
    if transparent:
        lc = "white"
        plt.rcParams["text.color"] = "white"
        plt.rcParams["axes.labelcolor"] = "white"
        plt.rcParams["axes.edgecolor"] = "white"
        plt.rcParams["xtick.color"] = "white"
        plt.rcParams["ytick.color"] = "white"

    df = pd.DataFrame(deviations)

    plt.gcf()
    # plt.rcParams["figure.figsize"] = (12, 4)
    plt.rcParams["xtick.labelsize"] = 10

    plt.plot(np.linspace(56, 58, len(deviations)), df[1], label="Эксцентриситет")
    plt.plot(np.linspace(56, 58, len(deviations)), df[2], label="Наклонение")

    plt.xlabel(r"Наклонение $\circ$")
    plt.xticks(np.linspace(56, 58, 21), rotation=90)

    # plt.yticks([])

    plt.legend(loc="upper center", ncol=2, frameon=False)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("deviations.png", transparent=transparent)


# def plot_from_file(path):
#     transparent = True
#     df = pd.read_csv(path)
#
#     n_periods = int(path.split("-")[-1].split(".")[0])
#     t = df["a"].values.shape[0]
#     print(t)
#     n = 10
#     time_scale = np.linspace(0, t, df["a"].values.shape[0])
#     ticks = np.linspace(0, t, n + 1)
#     labels = np.linspace(0, n_periods, n + 1, dtype=int)
#
#     names = ["a", "e", "i", "O", "w"]
#     names_greek = ["a", "e", "i", r"$\Omega$", r"$\omega$"]
#     units = ["км", "", r"$\circ$", r"$\circ$", r"$\circ$"]
#
#     styles = {
#         "a": {"c": "black", "lw": .75},
#         "e": {"c": "black", "lw": .75},
#         "i": {"c": "black", "lw": .75},
#         "O": {"c": "black", "lw": .75, "ls": "", "marker": ".", "ms": 2.5, "alpha": 1},
#         "w": {"c": "black", "lw": .75, "ls": "", "marker": ".", "ms": 2.5, "alpha": 1}
#     }
#
#     # plt.gcf()
#     plt.rcParams["figure.figsize"] = (12, 4)
#     plt.rcParams["axes.labelsize"] = 12
#
#     if transparent:
#         for k in styles:
#             styles[k]["c"] = "white"
#         plt.rcParams["text.color"] = "white"
#         plt.rcParams["axes.labelcolor"] = "white"
#         plt.rcParams["axes.edgecolor"] = "white"
#         plt.rcParams["xtick.color"] = "white"
#         plt.rcParams["ytick.color"] = "white"
#
#     for i in range(len(names)):
#         if i < 2:
#             plt.plot(time_scale, df[names[i]].values, **styles[names[i]])
#         else:
#             plt.plot(time_scale, np.rad2deg(df[names[i]].values), **styles[names[i]])
#
#         plt.xticks(ticks, labels=labels)
#
#         plt.xlabel("Обороты")
#         plt.ylabel(f"{names_greek[i]}, {units[i]}" if units[i] != "" else f"{names_greek[i]}")
#
#         plt.grid(True)
#
#         plt.tight_layout()
#         plt.savefig(f"data/current/{names[i]}.png", transparent=transparent)
#         plt.clf()


def main():
    time_start = dt.now()
    orbit = parser.read_orbits("glonass")[0]
    # orbit[1] = 0

    models.run_not_perturbed(orbit, 1, "data/not_perturbed")
    models.run_not_perturbed(orbit, 3000, "data/not_perturbed")
    analyzer.analyze_precision()

    # models.glonass_circ(3000, "data/current")
    # models.gps_circ(3000, "data/current")
    # models.gps_el(3000, "data/current")
    # plotter.plot_all_sep("data/current/current.csv", n_periods=3000)

    # models.orbits_states()
    # plotter.plot_orbits("data/orbits", shape="square")

    # variations.inc_variation(3000, "data\\elements\\data\\step-0.1", 55.5, 55.6, 0.1)
    # variations.analyze("data\\elements\\data\\step-1.0", "")
    # variations.analyze("data\\elements\\data\\step-0.1", "")

    # analyzer.analyze_deviations("data\\elements\\data\\step-0.1\\inc-55.60--p-3000.csv")
    # analyzer.analyze_deviations("data\\elements\\data\\step-0.1\\inc-56.00--p-3000.csv")
    # analyzer.analyze_deviations("data\\elements\\data\\step-0.1\\inc-56.50--p-3000.csv")

    # plotter.plot_all_sep("data\\elements\\data\\step-0.1\\inc-55.60--p-3000.csv", "data\\inc-55.60", n_periods=3000)
    # plotter.plot_all_sep("data\\elements\\data\\step-0.1\\inc-56.00--p-3000.csv", "data\\inc-56.00", n_periods=3000)
    # plotter.plot_all_sep("data\\elements\\data\\step-0.1\\inc-56.50--p-3000.csv", "data\\inc-56.50", n_periods=3000)
    # analyze_files()
    # plot_from_file("data/elements/data/nz-step-0.1/inc-57.60--p-3000.csv")

    # visibility_experiment()

    print(f"[+] Exiting program.\n"
          f"[+] Execution took: {(dt.now() - time_start).total_seconds()}")


if __name__ == '__main__':
    main()
