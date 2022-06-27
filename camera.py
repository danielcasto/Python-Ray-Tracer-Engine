from io import UnsupportedOperation
from numpy import array, dot
from numpy.linalg import norm
from math import isclose
from ray import Ray

class Camera:
    def __init__(self, w: array, v: array, u: array, e: array, ray_size: tuple[int, int]):
        self.w = w
        self.v = v
        self.u = u
        self.e = e
        self.ray_size = ray_size

    def take_picture(self, lights, shapes):
        # TODO currently unsupported
        raise UnsupportedOperation

    def get_solutions(self, shapes):
        # Finds ray intersection with shape and returns t('s)
        # TODO currently unsupported
        raise UnsupportedOperation


class ParallelCamera(Camera):
    def __init__(self, w: array, v: array, u: array, e: array, ray_size: tuple[int, int]):
        super().__init__(w, v, u, e, ray_size)
        self.set_basis(w, v, u, e)

        # set rays
        self.rays = []
        width = ray_size[0]
        height = ray_size[1]

        top_right_corner: array = array(e + (height//2)*v + (width//2)*u)
        
        for i in range(height):
            self.rays.append([])
            for j in range(width):
                self.rays[i].append(None)
        
        for i in range(height):
            for j in range(width):
                self.rays[i][(width-1)-j] = Ray(top_right_corner - i*v - j*u, -w)
    
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


class PerspectiveCamera(Camera):
    def __init__(self, w: array, v: array, u: array, e: array, d: float, ray_size: tuple[int, int]):
        super().__init__(w, v, u, e, ray_size)
        self.set_basis(w, v, u, e, d)

    def set_basis(self, w: array, v: array, u: array, e: array, d: float):
        self.w: array = w/norm(w)
        self.v: array = v/norm(v)
        self.u: array = u/norm(u)
        self.e: array = e

        try:
            assert isclose(dot(w, v), 0.0) and isclose(dot(v, u), 0.0) and isclose(dot(u, w), 0.0)
        except AssertionError:
            raise Exception(w, v, u, 'These three vectors are not orthogonal to each other')

        self.d: float = d

        return self