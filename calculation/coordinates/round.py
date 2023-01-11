from numpy import cos, sin
from numpy import power
from numpy.linalg import norm


def f_d(x_, gravitational_parameter,
        semimajor_axis, es,
        mean_orbital_speed,
        epoch_current, epoch_start):
    """
    Additional force caused by object

    Args:
        x_: Current coordinates of object under caused force
        gravitational_parameter: Gravitational parameter of object
        semimajor_axis: Semimajor axis of object
        es: Tuple of orthogonal vectors size of 3,
        that defines orbital plane of object
        mean_orbital_speed: Mean orbital speed of moving object
        epoch_current: Current epoch
        epoch_start: Starting epoch
    Returns:
        Force caused by moving object at moment t
    """
    x_d = x(semimajor_axis, es, mean_orbital_speed, epoch_current, epoch_start)
    return -gravitational_parameter * ((x_ - x_d) / power(norm(x_ - x_d), 3) + x_ / power(norm(x_d), 3))


def x(semimajor_axis,
      es,
      mean_orbital_speed,
      epoch_current, epoch_start):
    """
    Coordinates of object that moves on the round orbit around a body.

    Args:
        semimajor_axis: Semimajor axis of object
        es: Tuple of orthogonal vectors size of 3,
        that defines orbital plane of object
        mean_orbital_speed: Mean orbital speed of moving object
        epoch_current: Current epoch
        epoch_start: Starting epoch
    Returns:
        Coordinates of moving object on moment t
    """

    nu_ = nu(mean_orbital_speed, epoch_current, epoch_start)
    return semimajor_axis * (es[0] * cos(nu_) + es[1] * sin(nu_))


def nu(mean_orbital_speed,
       epoch_current, epoch_start):
    """
    Anomaly of object that moves on the round orbit around a body

    Args:
        mean_orbital_speed: Mean orbital speed of moving object
        epoch_current: Current epoch
        epoch_start: Starting epoch
    Returns:
        nu: Anomaly of moving object
    """
    return mean_orbital_speed * (epoch_current - epoch_start)
