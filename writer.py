import numpy as np
import csv
import os


def write_csv_es(elements, n_periods, output_path, current):
    # print(elements)
    inc = elements[0, 2]

    if current:
        filename = "current"
    else:
        filename = f"inc-{np.rad2deg(inc):.2f}--p-{n_periods}"

    with open(f"{output_path}\\{filename}.csv", "w", newline="") as file:
        header = ["a", "e", "i", "O", "w", "M"]

        writer = csv.writer(file)
        writer.writerow(header)

        for e in elements:
            writer.writerow(e)


def write_csv_states(states, n_periods, output_path):
    filename = f"states--p-{n_periods}.csv"

    with open(os.path.join(output_path, filename), "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["x", "y", "z", "vx", "vy", "vz"])

        for s in states:
            writer.writerow(s)
