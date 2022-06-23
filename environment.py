from typing import Any
from numpy import array


class Environment:
    def __init__(self, size: tuple[int, int]) -> None:
        self.size = size
    
    def add_light_source(self, light_type: str, intensity: float, pos: array, dir: array = None) -> Any:
        # TODO currently unsupported
        return self

    def add_triangle(self, v1: array, v2: array, v3: array, color: tuple[int, int, int]) -> Any:
        # TODO currently unsupported
        return self
    
    def add_sphere(self, center: array, radius: float, color: tuple[int, int, int]) -> Any:
        # TODO currently unsupported
        return self
    
    def with_parallel_camera(self, w: array, v: array, u: array, e: array) -> Any:
        # TODO currently unsupported
        return self
    
    def with_perspective_camera(self, w: array, v: array, u: array, e: array, d: float) -> Any:
        # TODO currently unsupported
        return self
    
    def use_camera(self) -> None:
        # TODO currently unsupported
        pass