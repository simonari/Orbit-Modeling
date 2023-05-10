import numpy as np

from constants_lib import attractor_radius


class SurfaceObject:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.radius = attractor_radius

        self.cs_rec = np.zeros(3)
        self.__geocentric_to_rectangular()

    def __geocentric_to_rectangular(self):
        self.cs_rec[0] = np.cos(self.longitude) * np.cos(self.latitude)
        self.cs_rec[1] = np.sin(self.longitude) * np.cos(self.latitude)
        self.cs_rec[2] = np.sin(self.latitude)

        self.cs_rec *= attractor_radius
