import numpy as np
import numpy.linalg as linalg
from scipy.integrate import solve_ivp

from constants_lib import precision as prec
from .OrbitObject import OrbitObject


class OrbitObjectPerturbed1(OrbitObject):
    def __init__(self, kepler_elements, perturbation_body_params):
        super().__init__(kepler_elements)
        self.mu_p = perturbation_body_params.mu
        self.e1e2_p = perturbation_body_params.e1e2
        self.a_p = perturbation_body_params.a
        self.n_p = perturbation_body_params.n


    def force_perturbation(self, state, epoch_current):
        """Additional force caused by object
        Args:
            state: State of an object
            epoch_current: Current epoch
        Returns:
            Force caused by moving object at a moment t
        """
        x = state[:3]
        nu_ = self.n_p * epoch_current

        x_p = self.a_p * (self.e1e2_p[0] * np.cos(nu_) + self.e1e2_p[1] * np.sin(nu_))

        matrix = np.array(
            [
                [.998502177e+0, -.547119902e-1, .000000000e+0],
                [.498452152e-1, .909682790e+0, .412301681e+0],
                [-.225578455e-1, -.411684126e+0, .911047378e+0],
            ]
        )
        x_p = matrix.dot(x_p)
        # x_p[2] = 0

        return -self.mu_p * ((x - x_p) / np.power(linalg.norm(x - x_p), 3) +
                             x_p / np.power(linalg.norm(x_p), 3))

    def f_p(self, t, state):
        t_jd = float(t / 86400)

        f_add = self.force_perturbation(state, t_jd)

        result = self.f(t, state)
        result[3:] += f_add

        return result

    def calculate_coordinates(self, t0_s=0, n=1):
        state = np.hstack((self.cs_rec, self.vs_rec))

        solution = solve_ivp(self.f_p,
                        (t0_s, n * self.T),
                        state,
                        method="DOP853",
                        rtol=prec * 1e-1,
                        atol=prec,
                        )

        self.cs_rec, self.vs_rec = np.hsplit(solution.y.transpose()[-1], 2)
        self.rectangular_to_kepler(self.cs_rec, self.vs_rec)

        return solution
