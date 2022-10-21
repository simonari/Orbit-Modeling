# types
from numpy import nditer
from numpy import uint16 as int

# functions
from numpy import linspace, zeros
from numpy import meshgrid

# classes
from Classes.OrbitObject import OrbitObject

# constants
from numpy import pi
from constants_lib import gravitational_parameter, attractor_radius, precision


def calc_visibility_of_group(groups, number_of_latitude_points, number_of_longitude_points):
    _map = zeros((number_of_longitude_points, number_of_latitude_points), dtype=int)

    latitude_array = linspace(-pi/2, pi/2, number_of_latitude_points)
    longitude_array = linspace(0, 2*pi, number_of_longitude_points)

    latitude_mesh, longitude_mesh = meshgrid(latitude_array, longitude_array)

    for orbit_idx, group in enumerate(groups):
        chosen_orbit = group.copy()
        print(f"[+] Currently working on {orbit_idx + 1} orbit")

        satellite = OrbitObject(gravitational_parameter, precision, *chosen_orbit)
        satellite.set_attractor_radius(attractor_radius)

        mesh_iterator = nditer(latitude_mesh, flags=['multi_index'])
        while not mesh_iterator.finished:
            idx_lon, idx_lat = mesh_iterator.multi_index
            if satellite.is_visible(latitude_mesh[idx_lon][idx_lat], longitude_mesh[idx_lon][idx_lat]):
                _map[idx_lat][idx_lon] += 1

            mesh_iterator.iternext()

    return _map
