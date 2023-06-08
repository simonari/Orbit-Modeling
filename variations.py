import os

import numpy as np
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt

from Classes.OrbitObjectPerturbed1 import OrbitObjectPerturbed1

from attractors import earth

import parser
import writer

import gc

def inc_variation(n_periods, output_path, a, b, step):
    chosen_orbit = parser.read_orbits()[0]

    with tqdm(total = int((b - a) / step)) as pbar:
        for inc_iter in np.arange(a, b, step):
            inc = np.deg2rad(inc_iter)
            chosen_orbit[2] = inc

            sat = OrbitObjectPerturbed1(chosen_orbit, earth)
            sol = sat.calculate_coordinates(n=n_periods)

            cs, vs = np.hsplit(sol.y.T, 2)

            elements = np.zeros((cs.shape[0], 6))

            for i in range(cs.shape[0]):
                elements[i] = sat.rectangular_to_kepler(cs[i], vs[i])

            writer.write_csv_es(elements, n_periods, output_path, current=False)

            pbar.update(1)
            del elements
            gc.collect()


def analyze(input_path, output_path):
    files = os.listdir(input_path)

    deviations = []

    inc_start, inc_end = float(files[0].split("-")[1]), float(files[-1].split("-")[1])

    pbar = tqdm(total=len(files))
    for file in files:
        df = pd.read_csv(os.path.join(input_path, file))

        for val in df:
            df[val] -= df[val].values[0]
            df[val] = abs(df[val])

        deviations.append(df.describe().loc["max"].to_numpy())
        pbar.update(1)

    # plt.rcParams["ytick.labelleft"] = False

    df = pd.DataFrame(deviations)

    # plt.gcf()
    plt.rcParams["figure.figsize"] = (12, 6)
    plt.rcParams["xtick.labelsize"] = 10

    fig, ax_e = plt.subplots()
    ax_inc = ax_e.twinx()

    ax_e.plot(np.linspace(inc_start, inc_end, len(deviations)), df[1], label="Эксцентриситет", ls="--", c="black")
    ax_inc.plot(np.linspace(inc_start, inc_end, len(deviations)), np.rad2deg(df[2]), label="Наклонение", ls="-", c="black")

    ax_e.set_ylabel("Эксцентриситет")
    ax_inc.set_ylabel(r"Наклонение, $\circ$")

    ax_e.set_xlabel(r"Начальное наклонение $\circ$")
    ax_e.set_xticks(np.linspace(inc_start, inc_end, len(files)), rotation=90)

    fig.legend(loc="upper center", ncol=2, frameon=False)
    # fig.legend()
    plt.grid(True)
    # plt.tight_layout()
    plt.savefig("deviations.png")
    plt.show()