from io import UnsupportedOperation
from numpy import array

class Ray:
    def __init__(self, origin, direction):
        self.origin: array = origin
        self.direction: array = direction