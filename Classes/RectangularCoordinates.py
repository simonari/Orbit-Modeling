from numpy import array


class RectangularCoordinates:
    def __init__(self, *args):
        if len(args) > 0:
            if isinstance(args[0], (list, type(array))):
                args = args[0]

        number_of_coordinates = len(args)

        if number_of_coordinates == 0:
            self.x = 0
            self.y = 0
            self.z = 0

        if number_of_coordinates == 1:
            self.x = args[0]
            self.y = 0
            self.z = 0

        if number_of_coordinates == 2:
            self.x = args[0]
            self.y = args[1]
            self.z = 0

        if number_of_coordinates == 3:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]

        if number_of_coordinates > 3:
            raise IndexError(f"Needed 3 or less components. {number_of_coordinates} was given")
        else:
            self.__to_list()

    def __repr__(self):
        return f"{self.x} {self.y} {self.z}"

    def __to_list(self):
        self.coordinates = [self.x, self.y, self.z]
