import numpy as np

from Classes.AttractorParameters import AttractorParameters


moon = AttractorParameters(
    mu=4902.801076,
    r=1738
)

earth = AttractorParameters(
    a=384400.0,
    n=.229970839,
    e1e2=(np.array([ .781828867,  .567420842,  .244151592]),
          np.array([-.617632360,  .715518303,  .315141549])),
    mu=398600.43560
)
