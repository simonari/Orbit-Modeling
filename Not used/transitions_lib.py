# importing mpmath module by types, methods and constants
from mpmath import mpf, matrix
from mpmath import sin, cos, sqrt, atan2, atan, power 
from mpmath import pi

from simple_iterations import simple_iterations
from equations import kepler_equation_right_part

from constants_lib import gravitational_parameter as grav_parameter, precision


def rectangular_to_kepler(coordinates, velocities, gravitational_parameter=grav_parameter):
    radius = mpf()
    for coordinate in coordinates:
        radius += power(coordinate, 2)
    radius = sqrt(radius)

    velocity2 = mpf()
    for velocity in velocities:
        velocity2 += power(velocity, 2)

    energy_integral = mpf(velocity2 / 2 - gravitational_parameter / radius)

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
        laplace_integrals[i] -= gravitational_parameter * coordinates[i] / radius

    laplace_integral = 0
    for integral in laplace_integrals:
        laplace_integral += power(integral, 2)
    laplace_integral = sqrt(laplace_integral)

    semimajor_axis = -gravitational_parameter / (2 * energy_integral)  # 1
    eccentricity = laplace_integral / gravitational_parameter  # 2

    inclination_cos = area_integrals[2] / area_integral
    inclination_sin = sqrt(1 - power(inclination_cos, 2))
    inclination = atan(inclination_sin / inclination_cos)  # 3

    longitude_of_ascending_node_sin = area_integrals[0] / (area_integral * inclination_sin)
    longitude_of_ascending_node_cos = -area_integrals[1] / (area_integral * inclination_sin)
    longitude_of_ascending_node = 2 * pi + atan2(longitude_of_ascending_node_sin, longitude_of_ascending_node_cos)  # 4

    periapsis_argument_sin = laplace_integrals[2] / (laplace_integral * inclination_sin)
    periapsis_argument_cos = \
        laplace_integrals[0] / laplace_integral * longitude_of_ascending_node_cos + \
        laplace_integrals[1] / laplace_integral * longitude_of_ascending_node_sin
    periapsis_argument = 2 * pi + atan2(periapsis_argument_sin, periapsis_argument_cos)  # 5

    xv = mpf()
    for i in range(3):
        xv += coordinates[i] * velocities[i]

    eccentric_anomaly_sin = xv / (eccentricity * sqrt(gravitational_parameter * semimajor_axis))
    eccentric_anomaly_cos = (1 - radius / semimajor_axis) / eccentricity
    eccentric_anomaly = 2 * pi + atan2(eccentric_anomaly_sin, eccentric_anomaly_cos)

    mean_anomaly = eccentric_anomaly - eccentricity * eccentric_anomaly_sin  # 6

    kepler_elements = matrix(
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


def kepler_to_rectangular(semimajor_axis, eccentricity, inclination, l_asc_node, periapsis_argument, mean_anomaly,
                          gravitational_parameter=grav_parameter):

    starting_eccentric_anomaly = mean_anomaly
    eccentric_anomaly = simple_iterations(kepler_equation_right_part, starting_eccentric_anomaly, precision,
                                          eccentricity=eccentricity,
                                          mean_anomaly=mean_anomaly)

    true_anomaly = atan2(sqrt(1 - power(eccentricity, 2)) * sin(eccentric_anomaly),
                         (cos(eccentric_anomaly) - eccentricity))

    latitude_arg = periapsis_argument + true_anomaly
    orbital_parameter = semimajor_axis * (1 - power(eccentricity, 2))
    radius = orbital_parameter / (1 + eccentricity * cos(true_anomaly))
    coordinates = []

    alpha = cos(latitude_arg) * cos(l_asc_node) - sin(latitude_arg) * sin(l_asc_node) * cos(inclination)
    betta = cos(latitude_arg) * sin(l_asc_node) + sin(latitude_arg) * cos(l_asc_node) * cos(inclination)
    gamma = sin(latitude_arg) * sin(inclination)

    coordinates.append(alpha * radius)
    coordinates.append(betta * radius)
    coordinates.append(gamma * radius)

    velocities = []

    alpha_ = -sin(latitude_arg) * cos(l_asc_node) - cos(latitude_arg) * sin(l_asc_node) * cos(inclination)
    betta_ = -sin(latitude_arg) * sin(l_asc_node) + cos(latitude_arg) * cos(l_asc_node) * cos(inclination)
    gamma_ = cos(latitude_arg) * sin(inclination)

    velocities. \
        append(sqrt(gravitational_parameter / orbital_parameter) * (alpha * eccentricity * sin(true_anomaly) +
                                                                    alpha_ * (1 + eccentricity * cos(true_anomaly))))
    velocities. \
        append(sqrt(gravitational_parameter / orbital_parameter) * (betta * eccentricity * sin(true_anomaly) +
                                                                    betta_ * (1 + eccentricity * cos(true_anomaly))))
    velocities. \
        append(sqrt(gravitational_parameter / orbital_parameter) * (gamma * eccentricity * sin(true_anomaly) +
                                                                    gamma_ * (1 + eccentricity * cos(true_anomaly))))

    return matrix(coordinates), matrix(velocities)
