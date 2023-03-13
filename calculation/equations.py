from numpy import array
from numpy import sin
from numpy import power, sqrt, sum

from attractors import earth
from constants_lib import gravitational_parameter_moon as mu_m
from constants_lib import gravitational_parameter_earth as mu_e
from calculation.time import jdutil


def kepler_equation(eccentric_anomaly, mean_anomaly, eccentricity):
    return mean_anomaly + eccentricity * sin(eccentric_anomaly)


# def f(t, state):
#     """
#     Right part of motion's differential equation.
#     Args:
#             t: Time of given state
#         state: (r, v) vector, where r - coordinates, v - velocities
#     Returns:
#         Right part of differential equation
#     """
#     radius = sqrt(sum(power(state[:3], 2)))
#
#     return array([
#         state[3],
#         state[4],
#         state[5],
#         -mu_m * state[0] / power(radius, 3),
#         -mu_m * state[1] / power(radius, 3),
#         -mu_m * state[2] / power(radius, 3)
#     ])
