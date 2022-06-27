from numpy import array

class Triangle:
    def __init__(self, v1: array, v2: array, v3: array, color: tuple[int, int, int]):
        self.v1: array = v1
        self.v2: array = v2
        self.v3: array = v3
        self.color: tuple[int, int, int] = color

        try:
            assert color[0] <= 255 and color[1] <= 255 and color[2] <= 255
        except(AssertionError):
            raise Exception(color, 'Out of bounds color value(s), values must be: 0 <= value <= 255')


class Sphere:
    pass