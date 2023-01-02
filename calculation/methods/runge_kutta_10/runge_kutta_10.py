import numpy as np
from numpy import sum
from numpy import float64 as float
from numpy import array
from numpy import empty, zeros
from numpy import power

from constants_lib import precision
from .coefficients import alphas as a, betas as b, cs as c
from calculation.equations import f


class RK10:
    def __init__(self, x0, h):
        self.x0 = x0
        self.solution_shape = x0.shape[0]
        self.h = h

        self.step_current = 0
        self.step_number = 17

        self.approx_intermediate = zeros((self.step_number, self.solution_shape), dtype=float)
        self.approx = zeros((self.step_number, self.solution_shape), dtype=float)

    def approximation_intermediate(self, k):
        res = zeros(self.solution_shape)

        for j in range(k):
            res += b[k][j] * f(self.approx_intermediate[j])

        res = self.x0 + self.h * res
        self.approx_intermediate[k] = res

    def approximation(self):
        res = zeros(self.solution_shape)

        for k in range(self.step_number):
            self.approximation_intermediate(k)
            res += c[k] * f(self.approx_intermediate[k])

        res = self.x0 + self.h * res
        self.approx[self.step_current] = res

    def next_step(self):
        self.approximation()
        self.step_current += 1

    def solution(self):
        while self.step_current != self.step_number:
            self.next_step()

        return self.approx[-1]

    # def __init__(self, x0, h):
    #     self.x0 = x0
    #     self.h = h
    #
    #     self.steps = 17
    #     self.step_current = 1
    #
    #     self.approximations = empty((self.steps, 6), dtype=float)
    #     self.approximations_intermediate = empty((self.steps, 6), dtype=float)
    #
    #     self.solution_prev = float(0)
    #     self.h_calculated = float(0)
    #
    # def approximation_intermediate(self, k):
    #     s = zeros(self.x0.shape, dtype=float)
    #
    #     for j in range(k):
    #         s += b[k][j] * f(self.approximations[j])
    #     res = self.x0 + self.h * s
    #     self.approximations_intermediate[k] = self.x0 + self.h * s
    #
    # def approximation(self):
    #     s = zeros(self.x0.shape, dtype=float)
    #
    #     for k in range(self.step_current):
    #         self.approximation_intermediate(k)
    #         s += c[k] * f(self.approximations_intermediate[k])
    #
    #     self.approximations[self.step_current] = self.x0 + self.h * s
    #
    # def approximation_low_order(self):
    #     s = empty(self.x0.shape, dtype=float)
    #
    #     for k in range(self.step_current):
    #         s += c[k] * f(self.approximations[k])
    #
    #     return self.x0 + self.h * s
    #
    # def calculate_new_h(self, solution, solution_low_order):
    #     result = self.h
    #     result *= power(abs(precision / (solution - solution_low_order)), 1/11)
    #     self.h_calculated = result
    #     return result
    #
    # def solution(self):
    #     for self.step_current in range(self.steps):
    #         self.approximation()
    #
    #     result = self.approximations[-1]
    #     self.solution_prev = self.approximations[-1]
    #
    #     # h = self.calculate_new_h(self.approximations[-1], self.approximation_low_order())
    #     h = self.h / 360 * (self.approximations[16] - self.approximations[0])
    #     self.h_calculated = h
    #     return result, h
    #
    # def start(self):
    #     self.solution()
    #
    #     self.solution_prev = self.x0
    #
    # def next(self):
    #     self.step_current = 1
    #     self.x0 = self.solution_prev
    #     self.h = self.h_calculated
    #
    #     result, h = self.solution()
    #
    #     return result, h