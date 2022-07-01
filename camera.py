from io import UnsupportedOperation
from typing import Optional
from numpy import array, dot, empty, transpose
from numpy.linalg import norm
from math import isclose, sqrt
from ray import Ray
from shapes import Triangle, Sphere


# TODO Refactor to have vars for width and height rather than tuple, will make function calls less confusing

class Camera:
    # Note: 'Camera' is meant to be na abstract base class
    def __init__(self, w: array, v: array, u: array, e: array, ray_size: tuple[int, int]):
        self.w = w
        self.v = v
        self.u = u
        self.e = e
        self.ray_size = ray_size
        self.rays: list

    def take_picture(self, lights, shapes):
        # TODO refactor to account for lights
        picture = empty((self.ray_size[1], self.ray_size[0], 3)) # This is the dimensions that pygame uses
        solutions = transpose(self.get_solutions(shapes))
        print(type(solutions[0,0]))

        for i in range(self.ray_size[1]):
            for j in range(self.ray_size[0]):
                picture[i,j] = (255, 0, 0) if solutions[i,j] > 0 else (0,0,0)

        return picture

    def get_solutions(self, shapes):
        # Finds ray intersection with shape and returns np.array of t's or None if no intersection at that pixel
        solution_arr = empty(self.ray_size, dtype=float)

        height = solution_arr.shape[0]
        width = solution_arr.shape[1]

        for i in range(height):
            for j in range(width):
                sphere_t = None
                triangle_t = None

                potential_ts = []
                for shape in shapes:
                    if isinstance(shape, Sphere):
                            sphere_t = self.get_sphere_valid_solution(shape, self.rays[i][j])
                            if sphere_t is not None:
                                potential_ts.append(sphere_t)
                    elif isinstance(shape, Triangle):
                        triangle_t = self.get_triangle_valid_solution(shape, self.rays[i][j])
                        potential_ts.append(triangle_t)
                    else:
                        raise Exception(shape, 'This object is not a supported shape or is not a shape at all')

                if len(potential_ts) > 0:
                    solution_arr[i, j] = min(potential_ts)
                else:
                    solution_arr[i,j] = -1
        
        return solution_arr

    def get_sphere_valid_solution(self, sphere: Sphere, ray: Ray):
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
        o: array = ray.origin
        d: array = ray.direction
        c: array = sphere.center
        r: float = sphere.radius

        a: float = dot(d, d) # scalar
        b: float = 2*dot(d, (o-c)) # scalar
        c: float = dot((o-c), (o-c)) - r**2 # scalar

        ''' find the discriminant:
                * If discriminant is greater than 0, two solutions exist.
                * If disciminant is 0, one solution exists.
                * If disciminant is less than 0, no solution exists.
        '''
        discriminant: float = b**2 - 4*a*c
        
        t1 = Optional[float]
        t2 = Optional[float]

        #find t('s)
        if discriminant > 0:
            t1 = (-b + sqrt(discriminant))/2*a
            t2 = (-b - sqrt(discriminant))/2*a
        elif discriminant == 0:
            t1 = -b/2*a
            t2 = None
        else:
            t1 = None
            t2 = None

        # Then, validate t('s) and reduce to one t if valid set of solutions
        valid_t: Optional[float]

        if t1 is not None and t2 is not None:
            if t1 <= 0 or t2 <= 0:
                valid_t = None # We don't want to render the inside of a sphere
            else:
                valid_t = t1 if t1 <= t2 else t2
        elif t1 is not None:
            valid_t = t1 if t1 >= 0 else None
        else:
            valid_t = None

        # Finally, return t or None
        return valid_t

    def get_triangle_valid_solution(self, triangle, ray):
        # TODO currently unsupported
        raise UnsupportedOperation


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