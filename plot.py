import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

names = ["a", "e", "i", "O", "w"]
names_greek = ["a", "e", "i", r"$\Omega$", r"$\omega$"]
units = ["км", "", r"$\circ$", r"$\circ$", r"$\circ$"]

styles = {
    "a": {"c": "black", "lw": .75},
    "e": {"c": "black", "lw": .75},
    "i": {"c": "black", "lw": .75},
    "O": {"c": "black", "lw": .75, "ls": "", "marker": ".", "ms": 2.5, "alpha": 1},
    "w": {"c": "black", "lw": .75, "ls": "", "marker": ".", "ms": 2.5, "alpha": 1}
}


def plot_all_sep(path_input, path_output, shape="wide"):
    try:
        df = pd.read_csv(path_input)
    except FileNotFoundError:
        print("[!] File not found!")
        raise FileNotFoundError

    if shape == "wide":
        plt.rcParams["figure.figsize"] = (12, 4)
    elif shape == "square":
        plt.rcParams["figure.figsize"] = (6.4, 6.4)
    else:
        print("[!] Wrong shape!")
        print("[!] Available shapes: wide, square")
        print(f'[!] [{shape}] was given')
        return None

    plt.rcParams["axes.labelsize"] = 12

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