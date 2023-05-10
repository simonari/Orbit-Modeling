import numpy as np

from Classes.OrbitObject import OrbitObject


def visibility_satellites(orbits: np.ndarray, img_resolution: tuple):
    _map = np.zeros(img_resolution, dtype=int)
    lat_mesh, lon_mesh = np.meshgrid(np.linspace(-np.pi / 2, np.pi / 2, img_resolution[0]),
                                     np.linspace(0, 2 * np.pi, img_resolution[1]))

    for orbit_idx, orbit in enumerate(orbits):
        chosen_orbit = orbit.copy()
        print(f"[+] Currently working on {orbit_idx + 1} orbit", flush=True)

        satellite = OrbitObject(chosen_orbit)

        mesh_iterator = np.nditer(lat_mesh, flags=['multi_index'])
        while not mesh_iterator.finished:
            idx_lon, idx_lat = mesh_iterator.multi_index
            if satellite.is_visible(lat_mesh[idx_lon][idx_lat], lon_mesh[idx_lon][idx_lat]):
                _map[idx_lat][idx_lon] += 1

            mesh_iterator.iternext()

    return _map
