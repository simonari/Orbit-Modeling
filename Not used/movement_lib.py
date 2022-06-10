from constants_lib import gravitational_parameter as grav_parameter
from mpmath import sqrt, power


def kepler_movement(start_epoch, end_epoch,
                    kepler_elements,
                    gravitational_parameter=grav_parameter):

    semimajor_axis = kepler_elements[0]
    mean_anomaly = kepler_elements[5]

    mean_orbital_speed = sqrt(gravitational_parameter / power(semimajor_axis, 3))
    mean_anomaly = mean_orbital_speed * (end_epoch - start_epoch) + mean_anomaly

    kepler_elements_output = kepler_elements.copy()
    kepler_elements_output[5] = mean_anomaly
    return kepler_elements_output
