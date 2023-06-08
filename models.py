import numpy as np

from attractors import earth
from Classes.OrbitObject import OrbitObject
from Classes.OrbitObjectPerturbed1 import OrbitObjectPerturbed1

import datetime

import writer
import parser


def run_not_perturbed(orbit, n_periods, output_path, current=True):
    time_s = datetime.datetime.now()

    sat = OrbitObject(orbit)

    sol = sat.calculate_coordinates(n=n_periods)

    writer.write_csv_states(sol.y.T, n_periods, output_path)

    delta = datetime.datetime.now() - time_s
    delta = float(f"{(delta.microseconds // 1000)}") + delta.seconds * 1000
    unit = "milliseconds"

    print(f"[+] Integration with {n_periods} periods took {delta} {unit}")


def run(orbit, n_periods, output_path, current=True):
    sat = OrbitObjectPerturbed1(orbit, earth)

    sol = sat.calculate_coordinates(n=n_periods)
    cs, vs = np.hsplit(sol.y.transpose(), 2)

    es = np.zeros((cs.shape[0], 6))
    for i in range(cs.shape[0]):
        es[i] = sat.rectangular_to_kepler(cs[i], vs[i])

    writer.write_csv_es(es, n_periods, output_path, current)


def gps_circ(n_periods, output_path):
    orbit = parser.read_orbits("gps")[0]
    orbit[1] = 0
    orbit[2] = np.deg2rad(56.4)

    run(orbit, n_periods, output_path)

def gps_el(n_periods, output_path):
    orbit = parser.read_orbits("gps")[0]
    orbit[2] = np.deg2rad(56.4)

    run(orbit, n_periods, output_path)


def glonass_circ(n_periods, output_path):
    orbit = parser.read_orbits("glonass")[0]
    orbit[1] = 0
    orbit[2] = np.deg2rad(64.8)

    run(orbit, n_periods, output_path)


def glonass_el(n_periods, output_path):
    orbit = parser.read_orbits("glonass")[0]
    orbit[2] = np.deg2rad(64.8)

    run(orbit, n_periods, output_path)


def orbits_states():
    orbits = parser.read_orbits("gps")

    for i, orbit in enumerate(orbits):
        sat = OrbitObject(orbit)

        states = np.zeros((361, 6))
        step = 2 * np.pi / 360
        for j in range(361):
            sat.move_by_mean_anomaly(step)

            states[j] = np.hstack((sat.cs_rec, sat.vs_rec))

        writer.write_csv_states(states, 1, f"data\\orbits\\{i + 1}")
