import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

names = ["a", "e", "i", "O", "w", "M"]
names_greek = ["a", "e", "i", r"$\Omega$", r"$\omega$", "M"]
units = ["км", "", r"$\circ$", r"$\circ$", r"$\circ$", r"$\circ$"]

styles = {
    "a": {"c": "black", "lw": .75},
    "e": {"c": "black", "lw": 1.5},
    "i": {"c": "black", "lw": 1.5},
    "O": {"c": "black", "lw": .75, "ls": "", "marker": ".", "ms": 2.5, "alpha": 1},
    "w": {"c": "black", "lw": .75, "ls": "", "marker": ".", "ms": 2.5, "alpha": 1},
    "M": {"c": "black", "lw": .75, "ls": "", "marker": ".", "ms": 2.5, "alpha": 1}
}

# if transparent:
#     for k in styles:
#         styles[k]["c"] = "white"
#     plt.rcParams["text.color"] = "white"
#     plt.rcParams["axes.labelcolor"] = "white"
#     plt.rcParams["axes.edgecolor"] = "white"
#     plt.rcParams["xtick.color"] = "white"
#     plt.rcParams["ytick.color"] = "white"

def plot_all_sep(path_input, path_output=None, shape="wide", n_periods=None):
    try:
        df = pd.read_csv(path_input)
    except FileNotFoundError:
        print("[!] File not found!")
        raise FileNotFoundError


    if path_output is None:
        path_output = os.path.join(*path_input.split("/")[:-1])

    if shape == "wide":
        plt.rcParams["figure.figsize"] = (12, 6)
    elif shape == "square":
        plt.rcParams["figure.figsize"] = (6.4, 6.4)
    else:
        print("[!] Wrong shape!")
        print("[!] Available shapes: wide, square")
        print(f'[!] [{shape}] was given')
        return None

    plt.rcParams["axes.labelsize"] = 16
    if n_periods is None:
        n_periods = int(path_input.split("-")[-1].split(".")[0])

    t = df["a"].values.shape[0]

    n_ticks = 10
    time_scale = np.linspace(0, t, df["a"].values.shape[0])
    ticks = np.linspace(0, t, n_ticks + 1)
    labels = np.linspace(0, n_periods, n_ticks + 1, dtype=int)

    for i, name in enumerate(names):
        if i < 2:
            plt.plot(time_scale, df[name].values, **styles[name])
        else:
            plt.plot(time_scale, np.rad2deg(df[name].values), **styles[name])

        plt.xticks(ticks, labels=labels)

        plt.xlabel("Обороты")
        plt.ylabel(f"{names_greek[i]}, {units[i]}" if units[i] != "" else f"{names_greek[i]}")

        plt.grid(True)

        plt.tight_layout()
        plt.savefig(f"{path_output}/{name}.png")
        # plt.savefig(f"data/current/{names[i]}.png", transparent=transparent)
        plt.clf()

        print(f"[+] Plot {name} successfully saved.")


def plot_orbits(path_input, path_output=None, shape="wide", n_periods=None):
    directories = os.listdir(path_input)
    directories.sort()

    if path_output is None:
        path_output = os.path.join(*path_input.split("/")[:-1])

    if shape == "wide":
        plt.rcParams["figure.figsize"] = (12, 6)
    elif shape == "square":
        plt.rcParams["figure.figsize"] = (6.4, 6.4)
    else:
        print("[!] Wrong shape!")
        print("[!] Available shapes: wide, square")
        print(f'[!] [{shape}] was given')
        return None

    plt.rcParams["axes.labelsize"] = 16

    # if n_periods is None:
    #     n_periods = int(path_input.split("-")[-1].split(".")[0])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # _cs = ["b", "b", "b", "b", "b",
    #        "g", "g", "g", "g",
    #        "r", "r", "r", "r",
    #        "c", "c", "c", "c",
    #        "m", "m", "m", "m",
    #        "y", "y", "y", "y"]

    for i, d in enumerate(directories):
        ss = pd.read_csv(os.path.join(path_input, d, "states--p-1.csv")).values

        # c = _cs.pop(0)
        ax.plot(ss[:, 0], ss[:, 1], ss[:, 2], c="black")
        ax.scatter(ss[0, 0], ss[0, 1], ss[0, 2], c="black")


    ax.set_aspect("equal")
    ax.set_xlabel("x, км")
    ax.set_ylabel("y, км")
    ax.set_zlabel("z, км")
    # fig.tight_layout()

    plt.show()
