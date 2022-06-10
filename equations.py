from mpmath import sin


def kepler_equation_right_part(eccentric_anomaly, mean_anomaly, eccentricity):
    return mean_anomaly + eccentricity * sin(eccentric_anomaly)