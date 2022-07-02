from io import UnsupportedOperation
import numpy as np
from camera import ParallelCamera, PerspectiveCamera
from light_source import ConeLight, PointLight, DirectionalInfiniteLight
from shapes import Triangle, Sphere

class Environment:
    def __init__(self, size: tuple[int, int]):
        self.size: tuple[int, int] = size
        self.lights: list = []
        self.shapes: list = []
        self.camera = None
    
    def add_light_source(self, light_type: str, intensity: float, pos: np.array = None, direction: np.array = None, angle: float = None):
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

    def add_triangle(self, v1: np.array, v2: np.array, v3: np.array, color: tuple[int, int, int]):
        self.shapes.append(Triangle(v1, v2, v3, color))

        return self
    
    def add_sphere(self, center: np.array, radius: float, color: tuple[int, int, int]):
        self.shapes.append(Sphere(center, radius, color))

        return self
    
    def with_parallel_camera(self, w: np.array, v: np.array, u: np.array, e: np.array):
        self.camera: ParallelCamera = ParallelCamera(w, v, u, e, (self.size[1], self.size[0])) # More intuitive to read lists and arrays this way

        return self
    
    def with_perspective_camera(self, w: np.array, v: np.array, u: np.array, e: np.array, d: float):
        self.camera: PerspectiveCamera = PerspectiveCamera(w, v, u, e, d, (self.size[1], self.size[0])) # More intuitive to read lists and arrays this way

        return self
    
    def use_camera(self):
        if self.camera == None:
            raise Exception('You must set a camera before trying to use it: call with_parallel_camera or with_perspective_camera first')

        return self.camera.take_picture(self.lights, self.shapes)