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
    vs *= 1 / 3600

    state = np.array([*cs, *vs])
    print(f"Initial state: {state}")

    h = orbit.period / n
    h_hours = h / 3600
    solution = RK10(state, h)
    solution.start()

    for i in range(n):
        if i % 1000 == 0:
            print(f"Step {i}")
        # orbit.move_by_dt(h)
        # print(solution.h_current)
        solution.next()

    print(f"Solution made by Runge-Kutta: {solution.x_current}")

    print(f"Solution made by adding mean anomaly and transform from kepler to rectangular")
    print(orbit.rectangular_coordinates)
    print(orbit.rectangular_velocities.to_ndarray() / 3600)
    print(f"[+] Exiting program.\n"
          f"[+] Execution took: {(dt.now() - time_start).total_seconds()}")


if __name__ == '__main__':
    set_printoptions(precision=6, suppress=True)
    n = 10000
    cycle_number = 4
    main()
