from numpy import sin, cos

from Classes.Vector3 import Vector3
from constants_lib import attractor_radius


class SurfaceObject:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.radius = attractor_radius

        self.__geocentric_to_rectangular()

    def __geocentric_to_rectangular(self):
        self.x = self.radius * cos(self.longitude) * cos(self.latitude)
        self.y = self.radius * sin(self.longitude) * cos(self.latitude)
        self.z = self.radius * sin(self.latitude)

        self.rectangular_coordinates = Vector3(self.x, self.y, self.z)
