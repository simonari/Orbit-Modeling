import multiprocessing as mp

from numpy import float32 as float
from numpy import zeros
from numpy import deg2rad

import satellites_orbits as sorbits

from visibility_process import visibility_process


def visibility(img_resolution,
               cycle_number,
               path):
    orbits = sorbits.orbits

    cycle_step = zeros(6, dtype=float)
    cycle_step[5] = deg2rad(360, dtype=float) / cycle_number

    tasks = [[orbits + cycle_step * cycle_current,
              img_resolution,
              cycle_current,
              cycle_number,
              path]
             for cycle_current in range(cycle_number)]

    process_pool = mp.Pool(mp.cpu_count())
    process_pool.starmap(visibility_process, tasks)
    process_pool.close()
