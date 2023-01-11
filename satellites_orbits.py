import numpy as np
from numpy import float64 as float, array, deg2rad, stack


satellite_ng1_s1 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(60, dtype=float),
    deg2rad(270, dtype=float),
    np.deg2rad(0, dtype=float)
))

satellite_ng1_s2 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(60, dtype=float),
    deg2rad(270, dtype=float),
    deg2rad(90, dtype=float)
))

satellite_ng1_s3 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(60, dtype=float),
    deg2rad(270, dtype=float),
    deg2rad(180, dtype=float)
))

satellite_ng1_s4 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(60, dtype=float),
    deg2rad(270, dtype=float),
    deg2rad(270, dtype=float)
))

satellite_ng2_s1 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(180, dtype=float),
    deg2rad(270, dtype=float),
    deg2rad(30, dtype=float)
))

satellite_ng2_s2 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(180, dtype=float),
    deg2rad(270, dtype=float),
    deg2rad(120, dtype=float)
))

satellite_ng2_s3 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(180, dtype=float),
    deg2rad(270, dtype=float),
    deg2rad(210, dtype=float)
))

satellite_ng2_s4 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(180, dtype=float),
    deg2rad(270, dtype=float),
    deg2rad(300, dtype=float)
))

satellite_ng3_s1 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(300, dtype=float),
    deg2rad(270, dtype=float),
    deg2rad(60, dtype=float)
))

satellite_ng3_s2 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(300, dtype=float),
    deg2rad(270, dtype=float),
    deg2rad(150, dtype=float)
))

satellite_ng3_s3 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(300, dtype=float),
    deg2rad(270, dtype=float),
    deg2rad(240, dtype=float)
))

satellite_ng3_s4 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(300, dtype=float),
    deg2rad(270, dtype=float),
    deg2rad(330, dtype=float)
))

satellite_sg1_s1 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(0, dtype=float),
    deg2rad(90, dtype=float),
    deg2rad(0, dtype=float)
))

satellite_sg1_s2 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(0, dtype=float),
    deg2rad(90, dtype=float),
    deg2rad(90, dtype=float)
))

satellite_sg1_s3 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(0, dtype=float),
    deg2rad(90, dtype=float),
    deg2rad(240, dtype=float)
))

satellite_sg1_s4 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(0, dtype=float),
    deg2rad(90, dtype=float),
    deg2rad(330, dtype=float)
))

satellite_sg2_s1 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(120, dtype=float),
    deg2rad(90, dtype=float),
    deg2rad(30, dtype=float)
))

satellite_sg2_s2 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(120, dtype=float),
    deg2rad(90, dtype=float),
    deg2rad(120, dtype=float)
))

satellite_sg2_s3 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(120, dtype=float),
    deg2rad(90, dtype=float),
    deg2rad(210, dtype=float)
))

satellite_sg2_s4 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(120, dtype=float),
    deg2rad(90, dtype=float),
    deg2rad(300, dtype=float)
))

satellite_sg3_s1 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(240, dtype=float),
    deg2rad(90, dtype=float),
    deg2rad(60, dtype=float)
))

satellite_sg3_s2 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(240, dtype=float),
    deg2rad(90, dtype=float),
    deg2rad(150, dtype=float)
))

satellite_sg3_s3 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(240, dtype=float),
    deg2rad(90, dtype=float),
    deg2rad(240, dtype=float)
))

satellite_sg3_s4 = array((
    float(6952),
    float(0.7),
    deg2rad(56.4, dtype=float),
    deg2rad(240, dtype=float),
    deg2rad(90, dtype=float),
    deg2rad(330, dtype=float)
))

orbits = stack((satellite_ng1_s1, satellite_ng1_s2, satellite_ng1_s3, satellite_ng1_s4,
                satellite_ng2_s1, satellite_ng2_s2, satellite_ng2_s3, satellite_ng2_s4,
                satellite_ng3_s1, satellite_ng3_s2, satellite_ng3_s3, satellite_ng3_s4,
                satellite_sg1_s1, satellite_sg1_s2, satellite_sg1_s3, satellite_sg1_s4,
                satellite_sg2_s1, satellite_sg2_s2, satellite_sg2_s3, satellite_sg2_s4,
                satellite_sg3_s1, satellite_sg3_s2, satellite_sg3_s3, satellite_sg3_s4,
                ))
