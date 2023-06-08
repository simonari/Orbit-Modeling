import os
import numpy as np
import pandas as pd
from constants_lib import numbers_after_floating_point


def analyze_precision():
    directory = os.path.join(os.getcwd(), "data", "not_perturbed")
    files = os.listdir(directory)

    for file in files:
        df = pd.read_csv(os.path.join(directory, file))

        initial = df.values[0, :3]
        final = df.values[-1, :3]

        print(f"[+] Estimated error: {np.linalg.norm(initial - final):.2e}")
        print(f"[+] With used precision of {numbers_after_floating_point} on {file.split('-')[-1].split('.')[0]} periods")


def analyze_deviations(path_input):
    try:
        df = pd.read_csv(path_input)
    except FileNotFoundError:
        print("[!] File not found!")
        raise FileNotFoundError

    df["e"] = np.abs(df["e"].values - df["e"].values[0])
    df["i"] = np.abs(df["i"].values - df["i"].values[0])

    print(f"[+] Starting inclination = {path_input.split('-')[2]}")
    print(f"[+] Max deviation of eccentricity {np.max(df['e'].values):.2E}")
    print(f"[+] Max deviation of inclination {np.max(np.rad2deg(df['i'].values)):.2E}")