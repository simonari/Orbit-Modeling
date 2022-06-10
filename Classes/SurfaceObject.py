from mpmath import sin, cos

from Classes.Vector3 import Vector3


class SurfaceObject:
    def __init__(self, latitude, longitude, radius):
        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius

        self.__geocentric_to_rectangular()

    def __geocentric_to_rectangular(self):
        self.x = self.radius * cos(self.longitude) * cos(self.latitude)
        self.y = self.radius * sin(self.longitude) * cos(self.latitude)
        self.z = self.radius * sin(self.latitude)

        self.rectangular_coordinates = Vector3(self.x, self.y, self.z)
