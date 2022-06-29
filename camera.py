from io import UnsupportedOperation
from numpy import array, dot
from numpy.linalg import norm
from math import isclose
from ray import Ray
from shapes import Triangle, Sphere

class Camera:
    def __init__(self, w: array, v: array, u: array, e: array, ray_size: tuple[int, int]):
        self.w = w
        self.v = v
        self.u = u
        self.e = e
        self.ray_size = (ray_size[1], ray_size[0]) # originally was (width, height) bc of pygame, we want (height, width)

    def take_picture(self, lights, shapes):
        # TODO currently unsupported
        raise UnsupportedOperation

    def get_solutions(self, shapes):
        # Finds ray intersection with shape and returns t('s)
        solution_arr = array(self.ray_size)

        height = solution_arr.shape[0]
        width = solution_arr.shape[1]

        for i in range(height):
            for j in range(width):
                sphere_t = None
                triangle_t = None

                for shape in shapes:
                    if isinstance(shape, Sphere):
                        sphere_t = self.get_sphere_valid_solution(shape)
                    elif isinstance(shape, Triangle):
                        triangle_t = self.get_triangle_valid_solution(shape)
                    else:
                        raise Exception(shape, 'This object is not a supported shape or is not a shape at all')

    def get_sphere_valid_solution(self, sphere):
        ''' Finds ray intersection with a sphere, returns nearest t. If there is no solution, return None
                * A valid t must be greater than 0.
                * A set of valid t's must both be greater than 0, if only one is valid, the solutions are discarded (None is returned).
        
            Equation for find t: 
                t1 = (-b + sqrt(b^2 - 4ac))/2a, 
                t2 = (-b - sqrt(b^2 - 4ac))/2a
                
                Where:
                    a = (d*d)
                    b = 2d(o*c)
                    c = (o-c)*(o-c) - r^2
        '''
        
        ''' First, find the discriminant:
                * If discriminant is greater than 0, two solutions exist.
                * If disciminant is 0, one solution exists.
                * If disciminant is less than 0, no solution exists.
        '''

        # Then, find t('s)

        # Then, validate t('s) and reduce to one t if valid set of solutions

        # Finally, return t or None
        pass

    def get_triangle_valid_solution(self, triangle):
        pass


class ParallelCamera(Camera):
    def __init__(self, w: array, v: array, u: array, e: array, ray_size: tuple[int, int]):
        super().__init__(w, v, u, e, ray_size)
        self.set_basis(w, v, u, e)

        # set rays
        self.rays = []
        height = ray_size[0]
        width = ray_size[1]

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