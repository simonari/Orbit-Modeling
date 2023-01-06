import numpy as np
from numpy import sum
from numpy import float64 as float
from numpy import array
from numpy import empty, zeros
from numpy import power

from constants_lib import precision, numbers_after_floating_point as nafp
from .coefficients import alphas as a, betas as b, cs as c
from calculation.equations import f


class RK10:
    def __init__(self, x0, h):
        self.x0 = x0
        self.solution_shape = x0.shape[0]

        self.h_current = h
        self.x_current = x0

        self.h_before = h
        self.x_before = x0

        self.step_current = 0
        self.step_number = 17

        self.approximations_intermediate = zeros((self.step_number, self.solution_shape), dtype=float)
        self.approximations_intermediate[0] = x0
        self.approximations = zeros((self.step_number, self.solution_shape), dtype=float)
        self.approximations[0] = x0

    def reset_values(self):
        self.step_current = 0

        self.approximations_intermediate = zeros((self.step_number, self.solution_shape), dtype=float)
        self.approximations = zeros((self.step_number, self.solution_shape), dtype=float)

    def approximation_intermediate(self):
        res = zeros(self.solution_shape)

        for k in range(self.step_number):
            for j in range(k):
                res += b[k][j] * f(self.approximations_intermediate[j])

            self.approximations_intermediate[k] = self.x_current + self.h_current * res

    def approximation(self):
        res = zeros(self.solution_shape)

        for k in range(self.step_current):
            res += c[k] * f(self.approximations_intermediate[k])

        self.approximations[self.step_current] = self.x_current + self.h_current * res

    def calculate_h(self):
        h_new = self.h_current * (f(self.approximations_intermediate[1]) - f(self.approximations_intermediate[15])) / 360
        h_new = np.linalg.norm(h_new)
        # print(f"e_cal: {h_new}")
        h_new = self.h_current * power(precision / h_new, float(1 / 11))

        self.h_before = self.h_current
        self.h_current = h_new

    def next_step(self):
        self.approximation_intermediate()
        self.calculate_h()
        self.approximation()

        self.step_current += 1

    def solution(self):
        self.x_before = self.x_current

        while self.step_current != self.step_number:
            self.next_step()

        self.x_current = self.approximations[-1]

    def start(self):
        self.solution()

        self.x_current = self.x0

        self.reset_values()

    def next(self):
        self.solution()

        self.reset_values()
