from numpy import array
from numpy import sin
from numpy import sum, power, sqrt

from constants_lib import gravitational_parameter as mu


def kepler_equation(eccentric_anomaly, mean_anomaly, eccentricity):
    return mean_anomaly + eccentricity * sin(eccentric_anomaly)


def f(state):
    """
    Right part of motion's differential equation.
    Args:
        state: (r, v) vector, where r - coordinates, v - velocities.
    """
    radius = sqrt(sum(power(array([state[0], state[1], state[2]]), 2)))

    return array([
        state[3],
        state[4],
        state[5],
        -mu * state[0] / power(radius, 3),
        -mu * state[1] / power(radius, 3),
        -mu * state[2] / power(radius, 3)
    ])
