from numpy import inf

from scipy.integrate import solve_ivp

from calculation.equations import f as f

from constants_lib import precision


def int_ivp(y0, t, t0=0, max_step=inf, prec=precision):
    sol = solve_ivp(f, (t0, t), y0,
                    method="DOP853",
                    rtol=prec * 10e2, atol=prec,
                    max_step=max_step,
                    )
    return sol
