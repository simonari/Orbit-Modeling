from numpy import array
from constants_lib import numbers_after_floating_point

possible_iterations = numbers_after_floating_point * 5


def simple_iterations(equation, starting_approach, precision, *args, **kwargs):
    next_approach = equation(starting_approach, *args, **kwargs)
    iterations = 0
    approaches = array([starting_approach, next_approach])

    while abs(approaches[0] - approaches[1]) > precision:
    # while (abs(approaches[0] - approaches[1]) > precision) and (iterations < possible_iterations):
        approaches[0] = approaches[1]
        approaches[1] = equation(approaches[0], **kwargs)
        iterations += 1

    return approaches[1]
