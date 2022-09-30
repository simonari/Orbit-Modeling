import os

from mpmath import radians

from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from constants_lib import gravitational_parameter, attractor_radius, precision

from Classes.OrbitObject import OrbitObject

import satellites_groups as sg


def calc_visibility_of_group(groups, number_of_latitude_points, number_of_longitude_points):
    group_idx = 1
    orbit_idx = 1

    figure = plt.figure()
    axis = figure.add_subplot(111)

    # map_ = [[0 for i in range(number_of_longitude_points)] for j in range(number_of_latitude_points)]
    map_ = np.zeros((number_of_longitude_points, number_of_latitude_points), dtype=np.uint16)

    latitude_step = np.deg2rad(180, dtype=np.float32) / number_of_latitude_points
    longitude_step = np.deg2rad(360, dtype=np.float32) / number_of_longitude_points

    longitude_array = np.linspace(0, 360, number_of_longitude_points)
    latitude_array = np.linspace(-90, 90, number_of_latitude_points)

    lon_lat_mesh = np.meshgrid(longitude_array, latitude_array)

    # TODO Rework according to new data structure.
    # TODO Rework according to meshgrid
    for group in groups:
        chosen_orbit = group.copy()
        for mean_anomaly in group[5]:
            print(f"[+] Currently working on {group_idx} group: {orbit_idx} orbit")
            chosen_orbit[5] = mean_anomaly

            satellite = OrbitObject(gravitational_parameter, precision, *chosen_orbit)
            satellite.set_attractor_radius(attractor_radius)
            current_latitude, current_longitude = radians(-90), radians(0)

            point_idx = 1

            for i in range(number_of_latitude_points):
                for j in range(number_of_longitude_points):
                    if satellite.is_visible(current_latitude, current_longitude):
                        map_[i][j] += 1

                    point_idx += 1
                    if point_idx % 2500 == 0:
                        print(
                            f"[+] {point_idx}/{number_of_latitude_points * number_of_longitude_points} "
                            f"points processed")

                    current_longitude += longitude_step
                current_latitude += latitude_step
            orbit_idx += 1

        orbit_idx = 1
        group_idx += 1

    map_unique = np.unique(map_)
    
    im = axis.imshow(map_, cmap="hot", extent=[longitude_array[0], longitude_array[-1],
                                               latitude_array[0], latitude_array[-1]])

    colors = [im.cmap(im.norm(value)) for value in map_unique]
    patches = [mpatches.Patch(color=colors[i], label="{l}".format(l=map_unique[i])) for i in
               range(len(map_unique))]
    axis.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    print(f"[+] Heatmap plotted")

    return figure


def main():
    n = 10
    print(f"[+] Output image resolution: {n}x{n} pixels.")
    number_of_latitude_points = n
    number_of_longitude_points = n

    cycle_split_number = 8
    cycle_step = np.deg2rad(360, dtype=np.float32) / cycle_split_number

    folder = os.getcwd()
    folder = os.path.join(folder, f"data",
                          f"{number_of_latitude_points}x{number_of_longitude_points}",
                          f"{cycle_split_number}")

    if not os.path.exists(folder):
        os.makedirs(folder)

    for current_cycle, _ in enumerate(range(cycle_split_number)):
        print(f"[+] Current cycle: {current_cycle}")
        satellites_groups = sg.groups
        cycle_step_array = np.zeros(6, dtype=np.float32)
        cycle_step_array[5] = cycle_step

        satellites_groups += cycle_step_array

        figure = calc_visibility_of_group(satellites_groups, number_of_latitude_points, number_of_longitude_points)
        figure.axes[0].set_title(f"Cycle {current_cycle}/{cycle_split_number}")
        figure.savefig(os.path.join(folder, f"cycle {current_cycle}_{cycle_split_number}"), bbox_inches='tight')
        print(f"[+] Plot saved to a file.")

    print(f"[+] Exiting program.")


if __name__ == '__main__':
    np.set_printoptions(precision=3, suppress=True)
    main()
