from .OrbitObject import OrbitObject
from numpy import cos, sin
from numpy import power, sqrt
from numpy.linalg import norm

from numpy import array
from numpy import float64 as float

from scipy.integrate import solve_ivp

from calculation.time import jdutil
from constants_lib import precision as prec


class OrbitObjectPerturbed1(OrbitObject):
    def __init__(self, kepler_elements, perturbation_body_params):
        super().__init__(kepler_elements)
        self.mu_p = perturbation_body_params.mu
        self.e1e2_p = perturbation_body_params.e1e2
        self.a_p = perturbation_body_params.a
        self.n_p = perturbation_body_params.n

    def force_perturbation(self, epoch_current, epoch_start):
        """Additional force caused by object

        Args:
            that defines orbital plane of object
            epoch_current: Current epoch
            epoch_start: Starting epoch
        Returns:
            Force caused by moving object at moment t
        """
        x = self.rectangular_coordinates.to_ndarray()
        x_p = self.coordinates_perturbation(epoch_current, epoch_start)
        return -self.mu_p * ((x - x_p) / power(norm(x - x_p), 3) + x_p / power(norm(x_p), 3))

    def coordinates_perturbation(self, epoch_current, epoch_start):
        """
        Coordinates of object that moves on the round orbit around a body.

        Args:
            epoch_current: Current epoch
            epoch_start: Starting epoch
        Returns:
            Coordinates of moving object on moment t
        """

        nu_ = self.anomaly_perturbation(epoch_current, epoch_start)
        return self.a_p * (self.e1e2_p[0] * cos(nu_) + self.e1e2_p[1] * sin(nu_))

    def anomaly_perturbation(self, epoch_current, epoch_start):
        """
        Anomaly of object that moves on the round orbit around a body

        Args:
            epoch_current: Current epoch
            epoch_start: Starting epoch
        Returns:
            nu: Anomaly of moving object
        """
        return self.n_p * (epoch_current - epoch_start)

    def f_p(self, t, state, t0_jd):
        t_jd = t0_jd + float(t / 86400)
        f_add = self.force_perturbation(t_jd, t0_jd)

        radius = sqrt(sum(power(state[0:3], 2)))

        return array([
            state[3],
            state[4],
            state[5],
            -self.mu * state[0] / power(radius, 3) + f_add[0],
            -self.mu * state[1] / power(radius, 3) + f_add[1],
            -self.mu * state[2] / power(radius, 3) + f_add[2]
        ])

    def calculate_coordinates(self, t0_jd, t0_s=0, n=1):
        state = array([*self.rectangular_coordinates.to_ndarray(),
                       *self.rectangular_velocities.to_ndarray()])

        sol = solve_ivp(self.f_p, (t0_s, n * self.period), state,
                        method="DOP853",
                        rtol=prec * 10e2, atol=prec,
                        args=(t0_jd,))

        return sol
