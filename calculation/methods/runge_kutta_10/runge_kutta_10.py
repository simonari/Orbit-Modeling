from numpy import sum
from numpy import float64 as float
from numpy import array
from numpy import empty

from coeffcients import alphas as a, betas as b, cs as c
from calculation.equations import f


class RK10():
    def __init__(self, x0, t0, h):
        self.x0 = x0
        self.t0 = t0
        self.h = h

        self.steps = 17
        self.step_current = 1

        self.solutions = empty(17, dtype=float)

    def calculate_t(self, k):
        return self.t0 + a[k] * self.h

    def approximation_intermediate(self, k):
        s = empty(self.x0.shape, dtype=float)

        for j in range(k):
            s += b[j][k] * f(self.solutions[j])

        return self.x0 + self.h * s

    def approximation(self):
        s = empty(self.x0.shape, dtype=float)

        for k in range(self.step_current):
            s += c[k] * f(self.approximation_intermediate(k))

        return self.x0 + self.h * s

    def approximation_low_order(self):
        s = empty(self.x0.shape, dtype=float)

        for k in range(self.step_current):
            s += c[k] * f(self.solutions[k])

        return self.x0 + self.h * s
