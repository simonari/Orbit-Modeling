from OrbitObject import OrbitObject


class Satellite(OrbitObject):
    def __init__(self, kepler_elements):
        super().__init__(kepler_elements)