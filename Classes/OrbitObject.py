import numpy as np
import numpy.linalg as linalg

from Classes.SurfaceObject import SurfaceObject

from constants_lib import precision
from constants_lib import gravitational_parameter_moon as mu

from scipy.integrate import solve_ivp

class OrbitObject:
    """
    OrbitObject class object
    """
    cs_rec = np.zeros((3, 1))
    vs_rec = np.zeros((3, 1))

    def __init__(self, kepler_elements):
        self.a = float(kepler_elements[0])
        self.e = float(kepler_elements[1])
        # self.inc = np.deg2rad(kepler_elements[2])
        # self.w_lon = np.deg2rad(kepler_elements[3])
        # self.w_arg = np.deg2rad(kepler_elements[4])
        # self.anomaly_m = np.deg2rad(kepler_elements[5])
        self.inc = kepler_elements[2]
        self.w_lon = kepler_elements[3]
        self.w_arg = kepler_elements[4]
        self.anomaly_m = kepler_elements[5]

        self.cs_rec = np.zeros(3)
        self.vs_rec = np.zeros(3)

        self.n = np.sqrt(mu / np.power(self.a, 3))
        self.T = 2 * np.pi / self.n

        self.mu = mu
        self.kepler_to_rectangular()

    def get_elements(self):
        return np.array([
            self.a,
            self.e,
            self.inc,
            self.w_lon,
            self.w_arg,
            self.anomaly_m
        ])

    def kepler_equation_right_part(self, eccentric_anomaly):
        """
        Kepler's equation: E = M + e*sin(E)
        Right part of it: value = M + e*sin(E)
        """
        return self.anomaly_m + self.e * np.sin(eccentric_anomaly)

    def move_by_dt(self, dt):
        self.anomaly_m += self.n * dt
        self.kepler_to_rectangular()

    def move_by_epoch(self, t1, t2):
        self.anomaly_m += self.n * (t2 - t1)
        self.kepler_to_rectangular()

    def move_by_mean_anomaly(self, step):
        self.anomaly_m += step
        self.kepler_to_rectangular()

    def kepler_to_rectangular(self):
        a = self.a
        e = self.e
        inc = self.inc
        w_lon = self.w_lon
        w_arg = self.w_arg
        anomaly_m = self.anomaly_m

        ea = anomaly_m

        while True:
            sea = np.sin(ea)
            cea = np.cos(ea)
            ea_ = ea - (ea - e * sea - anomaly_m) / (1 - e * cea)
            if abs(ea - ea_) < precision: break
            ea = ea_

        r2a = (1 - e * cea)
        r = a * r2a

        sv = np.sqrt(1 - pow(e, 2)) * np.sin(ea) / r2a
        cv = (cea - e) / r2a
        v = np.arctan2(sv, cv)

        u = v + w_arg

        su = np.sin(u)
        cu = np.cos(u)
        so = np.sin(w_lon)
        co = np.cos(w_lon)
        sinc = np.sin(inc)
        cinc = np.cos(inc)

        self.cs_rec[0] = cu * co - su * so * cinc
        self.cs_rec[1] = cu * so + su * co * cinc
        self.cs_rec[2] = su * sinc
        self.cs_rec *= r

        mp = np.sqrt(mu / (a * (1 - np.power(e, 2))))
        vr = mp * e * sv / r
        vn = mp * (1 + e * cv)

        self.vs_rec[0] = (-su * co - cu * so * cinc)
        self.vs_rec[1] = (-su * so - cu * co * cinc)
        self.vs_rec[2] = cu * sinc
        self.vs_rec *= vn
        self.vs_rec += vr * self.cs_rec

    def rectangular_to_kepler(self, cs=cs_rec, vs=vs_rec, mu=mu):
        r = linalg.norm(cs)
        v2 = np.power(vs, 2).sum()

        ci = np.array([
            cs[1] * vs[2] - cs[2] * vs[1],
            cs[2] * vs[0] - cs[0] * vs[2],
            cs[0] * vs[1] - cs[1] * vs[0]
        ])

        c = linalg.norm(ci)

        fi = np.array([
            ci[2] * vs[1] - ci[1] * vs[2],
            ci[0] * vs[2] - ci[2] * vs[0],
            ci[1] * vs[0] - ci[0] * vs[1]
        ])

        fi += -mu * cs / r
        f = linalg.norm(fi)

        h = v2 / 2 - mu / r

        a = -mu / (2 * h)
        e = f / mu
        inc = np.arccos(ci[2] / c)
        w_lon = np.arctan2(ci[0], -ci[1])

        sw = (-fi[0] * ci[0] - fi[1] * ci[1]) / ci[2]
        cw = (-fi[0] * ci[1] + fi[1] * ci[0]) / c

        w_arg = np.arctan2(sw, cw)

        su = (-cs[0] * ci[0] - cs[1] * ci[1]) / ci[2]
        cu = (-cs[0] * ci[1] + cs[1] * ci[0]) / c

        u = np.arctan2(su, cu)
        v = u - w_arg

        sea = r * np.sin(v) / a / np.sqrt(1 - np.power(e, 2))
        cea = r * np.cos(v) / a + e
        ea = np.arctan2(sea, cea)
        anomaly_m = ea - e * sea

        self.inc = inc + 2 * np.pi if inc < 0 else inc
        self.w_lon = w_lon + 2 * np.pi if w_lon < 0 else w_lon
        self.w_arg = w_arg + 2 * np.pi if w_arg < 0 else w_arg
        self.anomaly_m = anomaly_m + 2 * np.pi if anomaly_m < 0 else anomaly_m

        return np.array([a, e, inc, w_lon, w_arg, anomaly_m])

    def is_visible(self, latitude, longitude):
        """
        Checking visibility of OrbitObject from position (latitude, longitude) of SurfaceObject
        """
        surface_object = SurfaceObject(latitude, longitude)
        u1 = (self.cs_rec - surface_object.cs_rec) / linalg.norm(self.cs_rec - surface_object.cs_rec)
        u2 = surface_object.cs_rec / linalg.norm(surface_object.cs_rec)
        angle = np.arccos(u1 @ u2)

        if angle <= np.pi / 2:
            return True
        else:
            return False

    def f(self, t, state):
        radius = linalg.norm(state[:3])

        return np.array([
            state[3],
            state[4],
            state[5],
            -mu * state[0] / np.power(radius, 3),
            -mu * state[1] / np.power(radius, 3),
            -mu * state[2] / np.power(radius, 3),
        ])

    def calculate_coordinates(self, n=1):
        state = np.hstack((self.cs_rec,
                           self.vs_rec))

        sol = solve_ivp(self.f,
                        (0, n * self.T),
                        state,
                        method="DOP853",
                        rtol=0,
                        atol=precision,
                        )

        self.cs_rec, self.vs_rec = np.hsplit(sol.y.transpose()[-1], 2)
        self.rectangular_to_kepler(self.cs_rec, self.vs_rec)

        return sol