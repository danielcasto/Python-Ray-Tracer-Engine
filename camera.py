from io import UnsupportedOperation
from numpy import array, dot
from numpy.linalg import norm
from math import isclose

class Camera:
    def __init__(self, w: array, v: array, u: array, e: array):
        self.set_basis(w, v, u, e)

    def set_basis(self, w: array, v: array, u: array, e: array):
        self.w: array = w/norm(w)
        self.v: array = v/norm(v)
        self.u: array = u/norm(u)
        self.e: array = e

        try:
            assert isclose(dot(w, v), 0.0) and isclose(dot(v, u), 0.0) and isclose(dot(u, w), 0.0)
        except AssertionError:
            raise Exception(w, v, u, 'These three vectors are not orthogonal to each other')

        return self

    def take_picture(self):
        # TODO currently unsupported
        raise UnsupportedOperation
        pass


class ParallelCamera(Camera):
    def __init__(self, w: array, v: array, u: array, e: array):
        super().__init__(w, v, u, e)


class PerspectiveCamera(Camera):
    def __init__(self, w: array, v: array, u: array, e: array, d: float):
        super().__init__(w, v, u, e)
        # TODO currently unsupported
        raise UnsupportedOperation

    def set_basis(self, w: array, v: array, u: array, e: array, d: float):
        # TODO currently unsupported
        raise UnsupportedOperation
        return self