import numpy as np

satellite_ng1_s1 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(60),
    np.deg2rad(270),
    np.deg2rad(0)
))

satellite_ng1_s2 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(60),
    np.deg2rad(270),
    np.deg2rad(90)
))

satellite_ng1_s3 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(60),
    np.deg2rad(270),
    np.deg2rad(180)
))

satellite_ng1_s4 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(60),
    np.deg2rad(270),
    np.deg2rad(270)
))

satellite_ng2_s1 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(180),
    np.deg2rad(270),
    np.deg2rad(30)
))

satellite_ng2_s2 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(180),
    np.deg2rad(270),
    np.deg2rad(120)
))

satellite_ng2_s3 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(180),
    np.deg2rad(270),
    np.deg2rad(210)
))

satellite_ng2_s4 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(180),
    np.deg2rad(270),
    np.deg2rad(300)
))

satellite_ng3_s1 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(300),
    np.deg2rad(270),
    np.deg2rad(60)
))

satellite_ng3_s2 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(300),
    np.deg2rad(270),
    np.deg2rad(150)
))

satellite_ng3_s3 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(300),
    np.deg2rad(270),
    np.deg2rad(240)
))

satellite_ng3_s4 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(300),
    np.deg2rad(270),
    np.deg2rad(330)
))

satellite_sg1_s1 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(0),
    np.deg2rad(90),
    np.deg2rad(0)
))

satellite_sg1_s2 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(0),
    np.deg2rad(90),
    np.deg2rad(90)
))

satellite_sg1_s3 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(0),
    np.deg2rad(90),
    np.deg2rad(240)
))

satellite_sg1_s4 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(0),
    np.deg2rad(90),
    np.deg2rad(330)
))

satellite_sg2_s1 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(120),
    np.deg2rad(90),
    np.deg2rad(30)
))

satellite_sg2_s2 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(120),
    np.deg2rad(90),
    np.deg2rad(120)
))

satellite_sg2_s3 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(120),
    np.deg2rad(90),
    np.deg2rad(210)
))

satellite_sg2_s4 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(120),
    np.deg2rad(90),
    np.deg2rad(300)
))

satellite_sg3_s1 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(240),
    np.deg2rad(90),
    np.deg2rad(60)
))

satellite_sg3_s2 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(240),
    np.deg2rad(90),
    np.deg2rad(150)
))

satellite_sg3_s3 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(240),
    np.deg2rad(90),
    np.deg2rad(240)
))

satellite_sg3_s4 = np.array((
    6952,
    0.7,
    np.deg2rad(56.4),
    np.deg2rad(240),
    np.deg2rad(90),
    np.deg2rad(330)
))

orbits = np.stack((satellite_ng1_s1, satellite_ng1_s2, satellite_ng1_s3, satellite_ng1_s4,
                   satellite_ng2_s1, satellite_ng2_s2, satellite_ng2_s3, satellite_ng2_s4,
                   satellite_ng3_s1, satellite_ng3_s2, satellite_ng3_s3, satellite_ng3_s4,
                   satellite_sg1_s1, satellite_sg1_s2, satellite_sg1_s3, satellite_sg1_s4,
                   satellite_sg2_s1, satellite_sg2_s2, satellite_sg2_s3, satellite_sg2_s4,
                   satellite_sg3_s1, satellite_sg3_s2, satellite_sg3_s3, satellite_sg3_s4,
                   ))
