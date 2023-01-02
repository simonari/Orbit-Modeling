from datetime import datetime as dt

import numpy as np
from numpy import set_printoptions

import Classes.OrbitObject
import satellites_orbits
# from visibility.visibility import visibility
from calculation.methods.runge_kutta_10.runge_kutta_10 import RK10


def main():
    time_start = dt.now()
    print(f"[+] Output image resolution: {n}x{n} pixels.")

    # visibility((n, n), cycle_number)

    orbit = satellites_orbits.satellite_ng1_s1
    orbit = Classes.OrbitObject.OrbitObject(orbit)
    cs = orbit.rectangular_coordinates
    vs = orbit.rectangular_velocities
    cs = cs.to_ndarray()
    vs = vs.to_ndarray()

    state = np.array([*cs, *vs])
    print(state)

    h = 2 * np.pi / n

    orbit.move_by_mean_anomaly(h)
    solution = RK10(state, h)

    print(solution.solution())
    print(orbit.rectangular_coordinates)
    print(orbit.rectangular_velocities)
    print(f"[+] Exiting program.\n"
          f"[+] Execution took: {(dt.now() - time_start).total_seconds()}")


if __name__ == '__main__':
    set_printoptions(precision=6, suppress=True)
    n = 10
    cycle_number = 4
    main()
