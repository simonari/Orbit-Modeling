from numpy import empty
from calculation.equations import f


def runge_kutta_4(state, step):
    """
    Runge-Kutta order of 4 integration method.

    Args:
        state: Vector of system's state.
        step:  Step of integration.

    Returns:
        Next solution which also will be state vector.
    """
    k1 = f(state)
    k2 = f(state + step / 2 * k1)
    k3 = f(state + step / 2 * k2)
    k4 = f(state + step * k3)

    return state + step / 6 * (k1 + (2 * k2) + (2 * k3) + k4)


def rk4(state, step, iterations):
    """
    Runge-Kutta order of 4 integration method.

    Args:
        state:      Initial vector of system's state.
        step:       Step of integration.
        iterations: Number of iterations.

    Returns:
        Array of solutions x_i, i = (0, iterations)
    """
    result = empty(iterations)

    rk_vec = state
    result[0] = rk_vec

    for i in range(1, iterations):
        rk_vec = runge_kutta_4(rk_vec, step)
        result[i] = rk_vec

    return result
