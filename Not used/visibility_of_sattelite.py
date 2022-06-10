from mpmath import matrix
from mpmath import sqrt
from mpmath import sin, cos, acos
from mpmath import pi

from constants_lib import attractor_radius


def spherical_to_rectangular(latitude, longitude, radius=attractor_radius):
    coordinates = matrix([
        radius * cos(longitude) * sin(latitude),
        radius * sin(longitude) * sin(latitude),
        radius * cos(latitude)
    ])

    return coordinates


def geocentric_to_rectangular(latitude, longitude, radius=attractor_radius):
    coordinates = matrix([
        radius * cos(longitude) * cos(latitude),
        radius * sin(longitude) * cos(latitude),
        radius * sin(latitude)
    ])

    return coordinates


def scalar_product(vector_1, vector_2=None):
    if vector_2 is None:
        vector_2 = vector_1.copy()

    product = 0
    for i in range(0, 3):
        product += vector_1[i] * vector_2[i]

    return product


def angle_between_vectors(vector_1, vector_2):
    angle = acos(scalar_product(vector_1, vector_2) / (sqrt(scalar_product(vector_1)) * sqrt(scalar_product(vector_2))))
    return angle


def is_visible(surface_coordinates, orbit_coordinates):
    if angle_between_vectors(surface_coordinates, orbit_coordinates) <= pi/2:
        return True
    else:
        return False