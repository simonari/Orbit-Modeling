# types
from numpy import nditer
from numpy import uint16 as int
from numpy import array

# functions
from numpy import linspace, zeros
from numpy import meshgrid

# classes
from Classes.OrbitObject import OrbitObject

# constants
from numpy import pi
from constants_lib import gravitational_parameter_moon, attractor_radius, precision


def visibility_satellites(orbits: array, img_resolution: tuple):
    _map = zeros(img_resolution, dtype=int)
    lat_mesh, lon_mesh = meshgrid(linspace(-pi / 2, pi / 2, img_resolution[0]),
                                  linspace(0,       2 * pi, img_resolution[1]))

    for orbit_idx, orbit in enumerate(orbits):
        chosen_orbit = orbit.copy()
        print(f"[+] Currently working on {orbit_idx + 1} orbit", flush=True)

        satellite = OrbitObject(chosen_orbit)

        mesh_iterator = nditer(lat_mesh, flags=['multi_index'])
        while not mesh_iterator.finished:
            idx_lon, idx_lat = mesh_iterator.multi_index
            if satellite.is_visible(lat_mesh[idx_lon][idx_lat], lon_mesh[idx_lon][idx_lat]):
                _map[idx_lat][idx_lon] += 1

            mesh_iterator.iternext()

    return _map
