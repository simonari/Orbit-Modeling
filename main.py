import os
import multiprocessing as mp

from datetime import datetime as dt
from datetime import timedelta

from numpy import set_printoptions

from numpy import float32 as float
from numpy import zeros

from numpy import deg2rad

import satellites_orbits as sorbits

from visibility_map_process import visibility_map_process


def main():
    time_start = dt.now()
    n = 100
    print(f"[+] Output image resolution: {n}x{n} pixels.")
    number_of_latitude_points = n
    number_of_longitude_points = n

    cycle_number = 8
    cycle_step = deg2rad(360, dtype=float) / cycle_number

    folder = os.getcwd()
    folder = os.path.join(folder, f"data",
                          f"{number_of_latitude_points}x{number_of_longitude_points}",
                          f"{cycle_number}")

    if not os.path.exists(folder):
        os.makedirs(folder)

    cycle_step_array = zeros(6, dtype=float)
    cycle_step_array[5] = cycle_step
    satellites_orbits = sorbits.orbits

    tasks = [[satellites_orbits + cycle_step_array * cycle_current,
              (n, n),
              cycle_current,
              cycle_number,
              folder]
             for cycle_current in range(cycle_number)]
    pool = mp.Pool(mp.cpu_count())
    pool.starmap(visibility_map_process, tasks)
    pool.close()

    print(f"[+] Exiting program.\n"
          f"[+] Execution took: {(dt.now() - time_start).total_seconds()}")


if __name__ == '__main__':
    set_printoptions(precision=3, suppress=True)
    main()
