from datetime import datetime as dt

import numpy as np
from numpy import set_printoptions

from numpy import float64 as float

from matplotlib import pyplot as plt

import Classes.OrbitObject
import satellites_orbits
from calculation.methods.DOP853 import DOP853


def energy_int(state):
    cs = state[:3]
    vs = state[3:]
    from constants_lib import gravitational_parameter_moon as mu
    r = np.sqrt(np.sum(np.power(cs, 2)))

    return np.sum(np.power(vs, 2)) - 2 * mu / r


def main():
    time_start = dt.now()

    orbit = satellites_orbits.satellite_ng1_s1
    orbit = Classes.OrbitObject.OrbitObject(orbit)
    cs = orbit.rectangular_coordinates
    vs = orbit.rectangular_velocities
    cs = cs.to_ndarray()
    vs = vs.to_ndarray()

    state = np.array([*cs, *vs])

    print(f"Initial state:\n{state}")
    print(f"Orbit period: {orbit.period}\n")
    h = orbit.period / n

    sol = DOP853.int_ivp(state, orbit.period, prec=float(1e-16))
    y = sol.y.transpose()[-1]
    print(np.abs(y - state))
    print(sol.t.shape[0])

    y = sol.y.transpose()
    x = np.hsplit(np.hsplit(y, 2)[0], 3)
    print(x)
    ax = plt.figure().add_subplot(111, projection='3d')
    ax.scatter(*x)
    ax.plot(*x)
    ax.set_aspect('equal')
    plt.show()

    # m = 11
    # precisions = [1e-6 * np.power(float(1e-1), i) for i in range(m)]
    # print(precisions)
    # solutions = []
    # steps = []
    #
    # for i in range(m):
    #     sol = DOP853.int_ivp(state, 1200 * orbit.period, prec=precisions[i])
    #     solutions.append(sol.y.transpose()[-1])
    #     steps.append(sol.t.shape[0])
    # solutions = np.array(solutions)

    # ds = np.abs(solutions - state)
    # print(ds[-1])
    # ds_norm = np.zeros(m)
    # for i, d in enumerate(ds):
    #     ds_norm[i] = np.linalg.norm(d)
    # print(ds_norm)
    #
    # fig, ax = plt.subplots(1)
    # ax.set_xscale('log')
    # ax.set_yscale('log')
    # print(steps)
    # for i in range(m):
    #     ax.scatter(steps[i], ds_norm[i], s=5, label=f"{precisions[i]:.0e}")
    # ax.set_xlabel(r"Number of steps")
    # ax.set_ylabel(r"$\Delta$")
    # ax.legend(title=r"$\epsilon$")
    # plt.show()

    print(f"[+] Exiting program.\n"
          f"[+] Execution took: {(dt.now() - time_start).total_seconds()} seconds")


if __name__ == '__main__':
    # set_printoptions(precision=4, suppress=True)
    n = 10000
    main()