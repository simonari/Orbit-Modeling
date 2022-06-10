from mpmath import matrix


def simple_iterations(equation, starting_approach, precision, *args, **kwargs):
    next_approach = equation(starting_approach, *args, **kwargs)

    approaches = matrix([starting_approach, next_approach])

    while abs(approaches[0] - approaches[1]) > precision:
        approaches[0] = approaches[1]
        approaches[1] = equation(approaches[0], **kwargs)

    return approaches[1]
