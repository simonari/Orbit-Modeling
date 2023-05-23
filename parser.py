import os
import numpy as np
import pandas as pd

def read_orbits():
    path_to_file = os.path.join(os.getcwd(), "data", "input", "orbits.txt")
    try:
        f = open(path_to_file, "r")
    except FileNotFoundError:
        print("[!] File not found.")
        return None

    elements = []
    while True:
        line = f.readline()
        if not line:
            break

        e = list(map(float, line.split(" ")))
        e[2:] = map(np.deg2rad, e[2:])

        elements.append(e)

    elements = np.array(elements)
    return elements


def read_current_elements():
    path_to_file = os.path.join(os.getcwd(), "data", "current", "elements.csv")

    try:
        df = pd.read_csv(path_to_file)
    except FileNotFoundError:
        print("[!] File not found.")
        return None

    return df


def read_stored_elements(directory, file):
    path_to_file = os.path.join(os.getcwd(), "data", "stored", directory, file)

    try:
        df = pd.read_csv(path_to_file)
    except FileNotFoundError:
        print("[!] File not found.")
        return None

    return df