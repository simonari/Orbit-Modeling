from Classes.AttractorParameters import AttractorParameters
from numpy import array
from numpy import float64 as float

moon = AttractorParameters(
    mu=float(4902.801076),
    r=float(1738)
)

earth = AttractorParameters(
    a=float(384400.0),
    n=float(.229970839),
    e1e2=(array([-.781828867, -.662735076, -.0189098618], dtype=float),
          array([0.684636126, -.662034129, -.0303143777], dtype=float)),
    mu=float(398600.43560)
)
