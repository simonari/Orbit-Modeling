import os

from numpy import set_printoptions

from numpy import float32 as float
from numpy import zeros

from numpy import deg2rad

import satellites_groups as sg

from visibility_group import calc_visibility_of_group
from visibility_map import visibility_map


def main():
    n = 25
    print(f"[+] Output image resolution: {n}x{n} pixels.")
    number_of_latitude_points = n
    number_of_longitude_points = n

    cycle_split_number = 8
    cycle_step = deg2rad(360, dtype=float) / cycle_split_number

    folder = os.getcwd()
    folder = os.path.join(folder, f"data",
                          f"{number_of_latitude_points}x{number_of_longitude_points}",
                          f"{cycle_split_number}")

    if not os.path.exists(folder):
        os.makedirs(folder)

    for current_cycle in range(cycle_split_number):
        print(f"[+] Current cycle: {current_cycle}")
        satellites_groups = sg.groups
        cycle_step_array = zeros(6, dtype=float)
        cycle_step_array[5] = cycle_step

        satellites_groups += cycle_step_array

        del cycle_step_array

        figure = visibility_map(calc_visibility_of_group(
            satellites_groups,
            number_of_latitude_points,
            number_of_longitude_points
        ))
        figure.axes[0].set_title(f"Cycle {current_cycle}/{cycle_split_number}")
        figure.savefig(os.path.join(folder, f"cycle {current_cycle}_{cycle_split_number}"), bbox_inches='tight')
        print(f"[+] Plot saved to a file.")

    print(f"[+] Exiting program.")


if __name__ == '__main__':
    set_printoptions(precision=3, suppress=True)
    main()
