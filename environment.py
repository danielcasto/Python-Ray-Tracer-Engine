from io import UnsupportedOperation
from numpy import array
from light_source import ConeLight, PointLight, DirectionalInfiniteLight
from shapes import Triangle, Sphere

class Environment:
    def __init__(self, size: tuple[int, int]):
        self.size: tuple[int, int] = size
        self.lights: list = []
        self.shapes: list = []
    
    def add_light_source(self, light_type: str, intensity: float, pos: array = None, direction: array = None, angle: float = None):
        light_type_lowercase = light_type.lower()

        if light_type_lowercase == 'cone':
            self.lights.append(ConeLight(intensity, pos, direction, angle))
        elif light_type_lowercase == 'point':
            self.lights.append(PointLight(intensity, pos))
        elif light_type_lowercase == 'directionalinfinite':
            self.lights.append(DirectionalInfiniteLight(intensity, direction))
        else:
            raise Exception(light_type, 'Invalid light_type. Can only be cone, point, or directionalinfinite')

        return self

    def add_triangle(self, v1: array, v2: array, v3: array, color: tuple[int, int, int]):
        self.shapes.append(Triangle(v1, v2, v3, color))

        return self
    
    def add_sphere(self, center: array, radius: float, color: tuple[int, int, int]):
        self.shapes.append(Sphere(center, radius, color))

        return self
    
    def with_parallel_camera(self, w: array, v: array, u: array, e: array):
        # TODO currently unsupported
        raise UnsupportedOperation
        return self
    
    def with_perspective_camera(self, w: array, v: array, u: array, e: array, d: float):
        # TODO currently unsupported
        raise UnsupportedOperation
        return self
    
    def use_camera(self):
        # TODO currently unsupported
        raise UnsupportedOperation
        pass