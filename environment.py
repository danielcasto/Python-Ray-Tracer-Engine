from io import UnsupportedOperation
from numpy import array
from camera import ParallelCamera, PerspectiveCamera
from light_source import ConeLight, PointLight, DirectionalInfiniteLight
from shapes import Triangle, Sphere

class Environment:
    def __init__(self, size: tuple[int, int]):
        self.size: tuple[int, int] = size
        self.lights: list = []
        self.shapes: list = []
        self.camera = None
    
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
        self.camera: ParallelCamera = ParallelCamera(w, v, u, e)

        return self
    
    def with_perspective_camera(self, w: array, v: array, u: array, e: array, d: float):
        self.camera: PerspectiveCamera = PerspectiveCamera(w, v, u, e, d)

        return self
    
    def use_camera(self):
        pass # TODO remove this when camera is working

        if self.camera == None:
            raise Exception('You must set a camera before trying to use it: call \
            with_parallel_camera or with_perspective_camera first')

        return self.camera.take_picture()