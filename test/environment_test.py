from environment import Environment
from light_source import ConeLight, PointLight, DirectionalInfiniteLight
from math import isclose

def environment_init_test():
    TEST_SIZE = (100, 100)
    environment = Environment(TEST_SIZE)

    assert environment.size == TEST_SIZE, \
        f'environment_init_test::  TEST_SIZE: {TEST_SIZE}, is not equal to env.size: {environment.size}'

def add_light_sources_test(np):
    TEST_SIZE = (100, 100)
    intensity = 100.0
    pos = np.array([1.0,0.0])
    direction = np.array([1.0,0.0])
    angle = 100.0
    
    environment = Environment(TEST_SIZE)
    environment.add_light_source('cone', intensity=intensity, pos=pos, direction=direction, angle=angle)
    assert isinstance(environment.lights[0], ConeLight) \
        and isclose(environment.lights[0].intensity, intensity) \
        and np.allclose(environment.lights[0].pos, pos) \
        and np.allclose(environment.lights[0].direction, direction) \
        and isclose(environment.lights[0].angle, angle), \
        f'''add_light_sources_test (ConeLight)::
                isinstance(environment.lights[0], ConeLight): {isinstance(environment.lights[0], ConeLight)},
                isclose(environment.lights[0].intensity, intensity): {isclose(environment.lights[0].intensity, intensity)},
                np.allclose(environment.lights[0].pos, pos): {np.allclose(environment.lights[0].pos, pos)}
                np.allclose(environment.lights[0].direction, direction): {np.allclose(environment.lights[0].direction, direction)}
                isclose(environment.lights[0].angle, angle): {isclose(environment.lights[0].angle, angle)}
        '''

    environment = Environment(TEST_SIZE)
    environment.add_light_source('directionalinfinite', intensity=intensity, direction=direction)
    assert isinstance(environment.lights[0], DirectionalInfiniteLight) \
        and isclose(environment.lights[0].intensity, intensity) \
        and np.allclose(environment.lights[0].direction, direction), \
        f'''add_light_sources_test (DirectionalInfinite)::
                isinstance(environment.lights[0], DirectionalInfinite): {isinstance(environment.lights[0], DirectionalInfiniteLight)},
                isclose(environment.lights[0].intensity, intensity): {isclose(environment.lights[0].intensity, intensity)},
                np.allclose(environment.lights[0].direction, direction): {np.allclose(environment.lights[0].direction, direction)}
        '''
    
    environment = Environment(TEST_SIZE)
    environment.add_light_source('point', intensity=intensity, pos=pos)
    assert isinstance(environment.lights[0], PointLight) \
        and isclose(environment.lights[0].intensity, intensity) \
        and np.allclose(environment.lights[0].pos, pos), \
        f'''add_light_sources_test (PointLight)::
                isinstance(environment.lights[0], PointLight): {isinstance(environment.lights[0], PointLight)}
                isclose(environment.lights[0].intensity, intensity): {isclose(environment.lights[0].intensity, intensity)}
                np.allclose(environment.lights[0].pos, pos): {np.allclose(environment.lights[0].pos, pos)}
        '''

def add_triangle_test(np):
    TEST_SIZE = (100, 100)
    v1 = np.array([1.0, 0.0, 0.0])
    v2 = np.array([0.0, 1.0, 0.0])
    v3 = np.array([0.0, 0.0, 1.0])
    color = (0,0,0)

    environment = Environment(TEST_SIZE)
    environment.add_triangle(v1, v2, v3, color)
    assert np.allclose(environment.shapes[0].v1, v1) \
        and np.allclose(environment.shapes[0].v2, v2) \
        and np.allclose(environment.shapes[0].v3, v3) \
        and environment.shapes[0].color == color, \
        f'''add_triangle_test::
                np.allclose(environment.shapes[0].v1, v1): {np.allclose(environment.shapes[0].v1, v1)}
                np.allclose(environment.shapes[0].v2, v2): {np.allclose(environment.shapes[0].v2, v2)}
                np.allclose(environment.shapes[0].v3, v3): {np.allclose(environment.shapes[0].v3, v3)}
                environment.shapes[0].color == color: {environment.shapes[0].color == color}
        '''