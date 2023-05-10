import multiprocessing as mp

import numpy as np

from satellites_orbits import orbits

from .visibility_process import visibility_process
from visibility.create_folder import create_folder


def visibility(img_resolution, cycle_number):
    folder = create_folder(img_resolution, cycle_number)

    cycle_step = np.zeros(6)
    cycle_step[5] = np.deg2rad(360) / cycle_number

    tasks = [[orbits + cycle_step * cycle_current,
              img_resolution,
              cycle_current,
              cycle_number,
              folder]
             for cycle_current in range(cycle_number)]

    process_pool = mp.Pool(mp.cpu_count())
    process_pool.starmap(visibility_process, tasks)
    process_pool.close()
