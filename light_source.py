from numpy import array

class DirectionalInfiniteLight:
    def __init__(self, intensity: float, direction: array):
        self.intensity: float = intensity
        self.direction: array = direction


class PointLight:
    def __init__(self, intensity: float, pos: array):
        self.intensity: float = intensity
        self.pos: array = pos


class ConeLight:
    def __init__(self, intensity: float, pos: array, direction: array, angle: float):
        self.intensity: float = intensity
        self.pos: array = pos
        self.direction: array = direction
        self.angle: array = angle