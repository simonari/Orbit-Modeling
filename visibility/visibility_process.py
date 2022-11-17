from .visibility_map import visibility_map
from .visibility_satellites import visibility_satellites


def visibility_process(orbits,
                       img_resolution,
                       cycle_current,
                       cycle_number,
                       path
                       ):
    _map = visibility_satellites(orbits, img_resolution)
    visibility_map(_map, cycle_current, cycle_number, path)
