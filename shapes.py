import numpy as np

class Triangle:
    def __init__(self, v1: np.array, v2: np.array, v3: np.array, color: tuple[int, int, int]):
        self.v1: np.array = v1
        self.v2: np.array = v2
        self.v3: np.array = v3
        self.color: tuple[int, int, int] = color

        try:
            assert color[0] <= 255 and color[1] <= 255 and color[2] <= 255
        except AssertionError:
            raise Exception(color, 'Out of bounds color value(s), values must be: 0 <= value <= 255')


class Sphere:
    def __init__(self, center: np.array, radius: float, color: tuple[int, int, int]):
        self.center: np.array = center
        self.radius: float = radius
        self.color: tuple[int, int, int] = color

        try:
            assert color[0] <= 255 and color[1] <= 255 and color[2] <= 255
        except AssertionError:
            raise Exception(color, 'Out of bounds color value(s), values must be: 0 <= value <= 255')