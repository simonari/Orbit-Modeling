from numpy import float64 as float
from numpy import sqrt
from numpy import arccos as acos
from numpy import array

from Classes.RectangularCoordinates import RectangularCoordinates


class Vector3(RectangularCoordinates):
    def __init__(self, *args):
        super().__init__(*args)
        self.length = self.module()

    def __mul__(self, other):
        result = float()
        for index in range(3):
            result += self.coordinates[index] * other.coordinates[index]

        return result

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __repr__(self):
        return f"{self.x} {self.y} {self.z}"

    def __len__(self):
        return 3

    def __iter__(self):
        return Vector3Iterator(self)

    def __getitem__(self, key):
        return self.coordinates[key]

    def module(self):
        return sqrt(self * self)

    def angle(self, other):
        return acos(self * other / (self.length * other.length))

    def to_ndarray(self):
        return array([self.x, self.y, self.z])


class Vector3Iterator:
    def __init__(self, vector):
        self.vector = vector
        self.index = 0

    def __next__(self):
        if self.index < len(self.vector):
            result = self.vector[self.index]

            self.index += 1

            return result
        raise StopIteration
