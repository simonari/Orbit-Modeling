from numpy import sqrt, power
from numpy import float64 as float, array
from numpy import sin, cos, arctan as atan, arctan2 as atan2

from numpy import pi

from Classes.Vector3 import Vector3
from Classes.SurfaceObject import SurfaceObject

from calculation.simple_iterations import simple_iterations

from constants_lib import precision
from constants_lib import gravitational_parameter_moon as mu

import numpy as np
from scipy.integrate import solve_ivp

class OrbitObject:
    """
    OrbitObject class object
    """
    rectangular_coordinates = Vector3()
    rectangular_velocities = Vector3()

    def __init__(self, kepler_elements):
        self.semimajor_axis = kepler_elements[0]
        self.eccentricity = kepler_elements[1]
        self.inclination = kepler_elements[2]
        self.longitude_of_ascending_node = kepler_elements[3]
        self.periapsis_argument = kepler_elements[4]
        self.mean_anomaly = kepler_elements[5]

        self.mean_orbital_speed = sqrt(mu / power(self.semimajor_axis, 3))
        self.period = 2 * pi / self.mean_orbital_speed

        self.mu = mu
        self.kepler_to_rectangular()

    def get_elements(self):
        return array([
            self.semimajor_axis,
            self.eccentricity,
            self.inclination,
            self.longitude_of_ascending_node,
            self.periapsis_argument,
            self.mean_anomaly
        ])

    def kepler_equation_right_part(self, eccentric_anomaly):
        """
        Kepler's equation: E = M + e*sin(E)
        Right part of it: value = M + e*sin(E)
        """
        return self.mean_anomaly + self.eccentricity * sin(eccentric_anomaly)

    def move_by_dt(self, dt):
        self.mean_anomaly += self.mean_orbital_speed * dt
        self.kepler_to_rectangular()

    def move_by_epoch(self, t1, t2):
        self.mean_anomaly += self.mean_orbital_speed * (t2 - t1)
        self.kepler_to_rectangular()

    def move_by_mean_anomaly(self, step):
        self.mean_anomaly += step
        self.kepler_to_rectangular()

    def kepler_to_rectangular(self):
        """
        Converts Kepler elements to rectangular coordinates
        """
        starting_eccentric_anomaly = self.mean_anomaly
        eccentric_anomaly = simple_iterations(self.kepler_equation_right_part,
                                              starting_eccentric_anomaly, precision)

        true_anomaly = atan2(sqrt(1 - power(self.eccentricity, 2)) * sin(eccentric_anomaly),
                             (cos(eccentric_anomaly) - self.eccentricity))

        latitude_arg = self.periapsis_argument + true_anomaly
        orbital_parameter = self.semimajor_axis * (1 - power(self.eccentricity, 2))
        radius = orbital_parameter / (1 + self.eccentricity * cos(true_anomaly))
        coordinates = []

        l_asc_node = self.longitude_of_ascending_node
        alpha = cos(latitude_arg) * cos(l_asc_node) - sin(latitude_arg) * sin(l_asc_node) * cos(self.inclination)
        betta = cos(latitude_arg) * sin(l_asc_node) + sin(latitude_arg) * cos(l_asc_node) * cos(self.inclination)
        gamma = sin(latitude_arg) * sin(self.inclination)

        coordinates.append(alpha * radius)
        coordinates.append(betta * radius)
        coordinates.append(gamma * radius)

        velocities = []

        alpha_ = -sin(latitude_arg) * cos(l_asc_node) - cos(latitude_arg) * sin(l_asc_node) * cos(self.inclination)
        betta_ = -sin(latitude_arg) * sin(l_asc_node) + cos(latitude_arg) * cos(l_asc_node) * cos(self.inclination)
        gamma_ = cos(latitude_arg) * sin(self.inclination)

        a = sqrt(mu / orbital_parameter)
        velocities.append(a * (alpha * self.eccentricity * sin(true_anomaly) +
                               alpha_ * (1 + self.eccentricity * cos(true_anomaly))))
        velocities.append(a * (betta * self.eccentricity * sin(true_anomaly) +
                               betta_ * (1 + self.eccentricity * cos(true_anomaly))))
        velocities.append(a * (gamma * self.eccentricity * sin(true_anomaly) +
                               gamma_ * (1 + self.eccentricity * cos(true_anomaly))))

        self.rectangular_coordinates = Vector3(coordinates)
        self.rectangular_velocities = Vector3(velocities)

    def rectangular_to_kepler(self):
        """
        Converts rectangular coordinates to Kepler elements
        """
        coordinates = self.rectangular_coordinates
        velocities = self.rectangular_velocities

        radius = float()
        for coordinate in self.rectangular_coordinates:
            radius += power(coordinate, 2)
        radius = sqrt(radius)

        velocity2 = float()
        for velocity in self.rectangular_velocities:
            velocity2 += power(velocity, 2)

        energy_integral = float(velocity2 / 2 - mu / radius)

        area_integrals = [
            coordinates[1] * velocities[2] - coordinates[2] * velocities[1],
            coordinates[2] * velocities[0] - coordinates[0] * velocities[2],
            coordinates[0] * velocities[1] - coordinates[1] * velocities[0]
        ]
        area_integral = 0
        for integral in area_integrals:
            area_integral += power(integral, 2)
        area_integral = sqrt(area_integral)

        laplace_integrals = [
            velocities[1] * area_integrals[2] - velocities[2] * area_integrals[1],
            velocities[2] * area_integrals[0] - velocities[0] * area_integrals[2],
            velocities[0] * area_integrals[1] - velocities[1] * area_integrals[0]
        ]
        for i in range(0, 3):
            laplace_integrals[i] -= mu * coordinates[i] / radius

        laplace_integral = 0
        for integral in laplace_integrals:
            laplace_integral += power(integral, 2)
        laplace_integral = sqrt(laplace_integral)

        semimajor_axis = -mu / (2 * energy_integral)  # 1
        eccentricity = laplace_integral / mu  # 2

        inclination_cos = area_integrals[2] / area_integral
        inclination_sin = sqrt(1 - power(inclination_cos, 2))
        inclination = atan(inclination_sin / inclination_cos)  # 3

        longitude_of_ascending_node_sin = area_integrals[0] / (area_integral * inclination_sin)
        longitude_of_ascending_node_cos = -area_integrals[1] / (area_integral * inclination_sin)
        longitude_of_ascending_node = atan2(longitude_of_ascending_node_sin, longitude_of_ascending_node_cos)  # 4

        periapsis_argument_sin = laplace_integrals[2] / (laplace_integral * inclination_sin)
        periapsis_argument_cos = \
            laplace_integrals[0] / laplace_integral * longitude_of_ascending_node_cos + \
            laplace_integrals[1] / laplace_integral * longitude_of_ascending_node_sin
        periapsis_argument = atan2(periapsis_argument_sin, periapsis_argument_cos)  # 5

        xv = float()
        for i in range(3):
            xv += coordinates[i] * velocities[i]

        eccentric_anomaly_sin = xv / (eccentricity * sqrt(mu * semimajor_axis))
        eccentric_anomaly_cos = (1 - radius / semimajor_axis) / eccentricity
        eccentric_anomaly = atan2(eccentric_anomaly_sin, eccentric_anomaly_cos)

        mean_anomaly = eccentric_anomaly - eccentricity * eccentric_anomaly_sin  # 6

        kepler_elements = array(
            [
                semimajor_axis,
                eccentricity,
                inclination,
                longitude_of_ascending_node,
                periapsis_argument,
                mean_anomaly
            ]
        )

        for element in kepler_elements:
            if element < 0:
                element += 2 * pi

        return kepler_elements

    def is_visible(self, latitude, longitude):
        """
        Checking visibility of OrbitObject from position (latitude, longitude) of SurfaceObject
        """
        surface_object = SurfaceObject(latitude, longitude)
        angle = Vector3.angle(self.rectangular_coordinates - surface_object.rectangular_coordinates,
                              surface_object.rectangular_coordinates)

        if angle <= pi / 2:
            return True
        else:
            return False

    def f(self, t, state):
        radius = np.linalg.norm(state)

        return array([
            state[3],
            state[4],
            state[5],
            -mu * state[0] / power(radius, 3),
            -mu * state[1] / power(radius, 3),
            -mu * state[2] / power(radius, 3),
        ])


    def calculate_coordinates(self, t0_jd, t0_s=0, n=1):
        state = array([*self.rectangular_coordinates.to_ndarray(),
                       *self.rectangular_velocities.to_ndarray()])

        sol = solve_ivp(self.f, (t0_s, n * self.period), state,
                        method="DOP853",
                        rtol=precision,
                        # atol=(
                        #     precision, precision, precision,
                        #     precision * 1e-2, precision * 1e-2, precision * 1e-2,
                        # )
                        atol=0,
                        # max_step=1
                        # dense_output=True,
                        # vectorized=True
                        )

        return sol