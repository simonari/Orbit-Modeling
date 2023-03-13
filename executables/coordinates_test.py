import datetime
from datetime import datetime as dt

import constants_lib
from calculation.time import jdutil

import numpy as np

from matplotlib import pyplot as plt

import satellites_orbits
from Classes.OrbitObject import OrbitObject
from Classes.OrbitObjectPerturbed1 import OrbitObjectPerturbed1
from attractors import earth


def main():
    coordinates()


def coordinates():
    time_start = dt.now()

    orbit = satellites_orbits.satellite_ng1_s1
    orbit = OrbitObject(orbit)
    cs = orbit.rectangular_coordinates
    vs = orbit.rectangular_velocities
    cs = cs.to_ndarray()
    vs = vs.to_ndarray()

    print(f"Initial cs: {cs}")
    print(f"Initial vs: {vs}")

    t0 = dt(2020, 1, 1, 12, 0, 0)
    t = t0 + datetime.timedelta(seconds=orbit.period)

    t0_jd = jdutil.datetime_to_jd(t0)
    N = 2
    sol = orbit.calculate_coordinates(t0_jd, n=N)
    cs, vs = np.hsplit(sol.y.transpose(), 2)
    print(cs.shape)

    e_int_0 = np.power(vs[0], 2).sum() / 2 - \
              constants_lib.gravitational_parameter_moon / np.sqrt(np.power(cs[0], 2).sum())
    e_int = np.power(vs[-1], 2).sum() / 2 - \
              constants_lib.gravitational_parameter_moon / np.sqrt(np.power(cs[-1], 2).sum())

    print(f"Energy integral difference:\n"
          f"{e_int - e_int_0}")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    n = cs.shape[0] // int(np.ceil(N))

    ax.plot(*np.hsplit(cs[:n], 3))
    ax.scatter(*np.hsplit(cs[:n], 3), c="red")
    ax.plot(*np.hsplit(cs[-n:], 3))

    print(f"Errors:\n"
          f"by coordinates: {cs[-1] - cs[0]}\n"
          f"by velocities: {vs[-1] - vs[0]}")

    print(f"[+] Exiting program.\n"
          f"[+] Execution took: {(dt.now() - time_start).total_seconds()}")

    plt.show()

def coordinates_perturbed():
    time_start = dt.now()

    orbit = satellites_orbits.satellite_ng1_s1
    orbit = OrbitObjectPerturbed1(orbit, earth)
    cs = orbit.rectangular_coordinates
    vs = orbit.rectangular_velocities
    cs = cs.to_ndarray()
    vs = vs.to_ndarray()

    t0 = dt(2020, 1, 1, 12, 0, 0)
    t = t0 + datetime.timedelta(seconds=orbit.period)

    t0_jd = jdutil.datetime_to_jd(t0)

    sol = orbit.calculate_coordinates(t0_jd, n=300)
    cs, vs = np.hsplit(sol.y.transpose(), 2)

    print(f"Errors:"
          f"by coordinates: {cs[-1] - cs[0]}\n"
          f"by velocities: {vs[-1] - vs[0]}")

    print(f"[+] Exiting program.\n"
          f"[+] Execution took: {(dt.now() - time_start).total_seconds()}")


def plots():
    time_start = dt.now()

    orbit = satellites_orbits.satellite_ng1_s1
    orbit = OrbitObjectPerturbed1(orbit, earth)
    cs = orbit.rectangular_coordinates
    vs = orbit.rectangular_velocities
    cs = cs.to_ndarray()
    vs = vs.to_ndarray()

    t0 = dt(2020, 1, 1, 12, 0, 0)
    t = t0 + datetime.timedelta(seconds=orbit.period)

    t0_jd = jdutil.datetime_to_jd(t0)
    sol = orbit.calculate_coordinates(t0_jd, n=100)
    cs, vs = np.hsplit(sol.y.transpose(), 2)



    coordinates_to_plot1 = np.hsplit(cs[:30], 3)
    coordinates_to_plot2 = np.hsplit(cs[-31:], 3)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    line1, = ax.plot(*coordinates_to_plot1, linewidth=1)
    line2, = ax.plot(*coordinates_to_plot2, linewidth=1)
    ax.set_aspect('equal')

    plt.show()

    print(f"[+] Exiting program.\n"
          f"[+] Execution took: {(dt.now() - time_start).total_seconds()}")

if __name__ == '__main__':
    main()
