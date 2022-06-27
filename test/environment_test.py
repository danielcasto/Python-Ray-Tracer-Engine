from environment import Environment
from light_source import ConeLight, PointLight, DirectionalInfiniteLight
from math import isclose

# TODO, put all the different class specific failure cases in their respective classes, it does not make sense to handle them here.

def environment_init_test():
    TEST_SIZE = (100, 100)
    environment = Environment(TEST_SIZE)

    assert environment.size == TEST_SIZE, \
        f'environment_init_test(valid params)::  TEST_SIZE: {TEST_SIZE}, is not equal to env.size: {environment.size}'

def add_light_sources_test(np):
    TEST_SIZE = (100, 100)
    intensity = 100.0
    pos = np.array([1.0, 0.0])
    direction = np.array([1.0, 0.0])
    angle = 100.0
    
    environment = Environment(TEST_SIZE)
    environment.add_light_source('cone', intensity=intensity, pos=pos, direction=direction, angle=angle)
    assert isinstance(environment.lights[0], ConeLight) \
        and isclose(environment.lights[0].intensity, intensity) \
        and np.allclose(environment.lights[0].pos, pos) \
        and np.allclose(environment.lights[0].direction, direction) \
        and isclose(environment.lights[0].angle, angle), \
        f'''add_light_sources_test (ConeLight, valid params)::
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
        f'''add_light_sources_test (DirectionalInfinite, valid params)::
                isinstance(environment.lights[0], DirectionalInfinite): {isinstance(environment.lights[0], DirectionalInfiniteLight)},
                isclose(environment.lights[0].intensity, intensity): {isclose(environment.lights[0].intensity, intensity)},
                np.allclose(environment.lights[0].direction, direction): {np.allclose(environment.lights[0].direction, direction)}
        '''
    
    environment = Environment(TEST_SIZE)
    environment.add_light_source('point', intensity=intensity, pos=pos)
    assert isinstance(environment.lights[0], PointLight) \
        and isclose(environment.lights[0].intensity, intensity) \
        and np.allclose(environment.lights[0].pos, pos), \
        f'''add_light_sources_test (PointLight, valid params)::
                isinstance(environment.lights[0], PointLight): {isinstance(environment.lights[0], PointLight)}
                isclose(environment.lights[0].intensity, intensity): {isclose(environment.lights[0].intensity, intensity)}
                np.allclose(environment.lights[0].pos, pos): {np.allclose(environment.lights[0].pos, pos)}
        '''
    
    # Invalid light type
    environment = Environment(TEST_SIZE)
    try:
        environment.add_light_source('somelight', intensity=intensity, pos=pos, direction=direction, angle=angle)
    except Exception as e:
        assert e.args == ('somelight', 'Invalid light_type. Can only be cone, point, or directionalinfinite'), \
            f'''add_light_sources_test(invalid light type)::
                    e.args == ('somelight', 'Invalid light_type. Can only be cone, point, or directionalinfinite'): 
                        {e.args == ('somelight', 'Invalid light_type. Can only be cone, point, or directionalinfinite')}
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
        f'''add_triangle_test(valid params)::
                np.allclose(environment.shapes[0].v1, v1): {np.allclose(environment.shapes[0].v1, v1)}
                np.allclose(environment.shapes[0].v2, v2): {np.allclose(environment.shapes[0].v2, v2)}
                np.allclose(environment.shapes[0].v3, v3): {np.allclose(environment.shapes[0].v3, v3)}
                environment.shapes[0].color == color: {environment.shapes[0].color == color}
        '''

    # Invalid color (greater than 255):
    greater_than_color_bound = (256,0,0)
    environment = Environment(TEST_SIZE)

    try:
        environment.add_triangle(v1, v2, v3, greater_than_color_bound)
    except Exception as e:
        assert e.args == (greater_than_color_bound, 'Out of bounds color value(s), values must be: 0 <= value <= 255'), \
            f'''add_triangle_test(greater than color bound)::
                    e.args == ((256,0,0), 'Out of bounds color value(s), values must be: 0 <= value <= 255'): 
                        {e.args == (greater_than_color_bound, 'Out of bounds color value(s), values must be: 0 <= value <= 255')}
            '''

    # Invalid color (less than 0):
    less_than_color_bound = (-1,0,0)
    environment = Environment(TEST_SIZE)

    try:
        environment.add_triangle(v1, v2, v3, less_than_color_bound)
    except Exception as e:
        assert e.args == (less_than_color_bound, 'Out of bounds color value(s), values must be: 0 <= value <= 255'), \
            f'''add_triangle_test(greater than color bound)::
                    e.args == ((-1,0,0), 'Out of bounds color value(s), values must be: 0 <= value <= 255'): 
                        {e.args == (less_than_color_bound, 'Out of bounds color value(s), values must be: 0 <= value <= 255')}
            '''


def add_sphere_test(np):
    TEST_SIZE = (100, 100)
    center = np.array([1.0, 0.0, 0.0])
    radius = 1.0
    color = (0,0,0)

    environment = Environment(TEST_SIZE)
    environment.add_sphere(center, radius, color)
    assert np.allclose(environment.shapes[0].center, center) \
        and isclose(environment.shapes[0].radius, radius) \
        and environment.shapes[0].color == color, \
        f'''add_sphere_test(valid params)::
                np.allclose(environment.shapes[0].center, center): {np.allclose(environment.shapes[0].center, center)}
                isclose(environment.shapes[0].radius, radius): {isclose(environment.shapes[0].radius, radius)}
                environment.shapes[0].color == color: {environment.shapes[0].color == color}
        '''
    
    # Invalid color (greater than 255):
    greater_than_color_bound = (256,0,0)
    environment = Environment(TEST_SIZE)

    try:
        environment.add_sphere(center, radius, greater_than_color_bound)
    except Exception as e:
        assert e.args == (greater_than_color_bound, 'Out of bounds color value(s), values must be: 0 <= value <= 255'), \
            f'''add_sphere_test(greater than color bound)::
                    e.args == ((256,0,0), 'Out of bounds color value(s), values must be: 0 <= value <= 255'): 
                        {e.args == (greater_than_color_bound, 'Out of bounds color value(s), values must be: 0 <= value <= 255')}
            '''

    # Invalid color (less than 0):
    less_than_color_bound = (-1,0,0)
    environment = Environment(TEST_SIZE)

    try:
        environment.add_sphere(center, radius, less_than_color_bound)
    except Exception as e:
        assert e.args == (less_than_color_bound, 'Out of bounds color value(s), values must be: 0 <= value <= 255'), \
            f'''add_sphere_test(greater than color bound)::
                    e.args == ((-1,0,0), 'Out of bounds color value(s), values must be: 0 <= value <= 255'): 
                        {e.args == (less_than_color_bound, 'Out of bounds color value(s), values must be: 0 <= value <= 255')}
            '''

def with_parallel_camera_test(np):
    TEST_SIZE = (100, 100)
    w = np.array([1.0, 0.0, 0.0])
    v = np.array([0.0, 1.0, 0.0])
    u = np.array([0.0, 0.0, 1.0])
    e = np.array([1.0, 0.0, 0.0])

    environment = Environment(TEST_SIZE)
    environment.with_parallel_camera(w, v, u, e)

    assert np.allclose(environment.camera.w, w) \
        and np.allclose(environment.camera.v, v) \
        and np.allclose(environment.camera.u, u) \
        and np.allclose(environment.camera.e, e), \
            f'''with_parallel_camera_test(valid params)::
                    np.allclose(environment.camera.w, w): {np.allclose(environment.camera.w, w)}
                    np.allclose(environment.camera.v, v): {np.allclose(environment.camera.v, v)}
                    np.allclose(environment.camera.u, u): {np.allclose(environment.camera.u, u)}
                    np.allclose(environment.camera.e, e): {np.allclose(environment.camera.e, e)}
            '''

def with_perspective_camera_test(np):
    TEST_SIZE = (100, 100)
    w = np.array([1.0, 0.0, 0.0])
    v = np.array([0.0, 1.0, 0.0])
    u = np.array([0.0, 0.0, 1.0])
    e = np.array([1.0, 0.0, 0.0])
    d = 10.0

    environment = Environment(TEST_SIZE)
    environment.with_perspective_camera(w, v, u, e, d)

    assert np.allclose(environment.camera.w, w) \
        and np.allclose(environment.camera.v, v) \
        and np.allclose(environment.camera.u, u) \
        and np.allclose(environment.camera.e, e) \
        and isclose(environment.camera.d, d), \
            f'''with_parallel_camera_test(valid params)::
                    np.allclose(environment.camera.w, w): {np.allclose(environment.camera.w, w)}
                    np.allclose(environment.camera.v, v): {np.allclose(environment.camera.v, v)}
                    np.allclose(environment.camera.u, u): {np.allclose(environment.camera.u, u)}
                    np.allclose(environment.camera.e, e): {np.allclose(environment.camera.e, e)}
                    isclose(environment.camera.d, d): {isclose(environment.camera.d, d)}
            '''

def use_camera_test(np):
    pass # TODO remove this after camera is working and finish this function
    TEST_SIZE = (100, 100)
    w = np.array([1.0, 0.0, 0.0])
    v = np.array([0.0, 1.0, 0.0])
    u = np.array([0.0, 0.0, 1.0])
    e = np.array([1.0, 0.0, 0.0])

    # Case with no camera set
    environment = Environment(TEST_SIZE)
    try:
        environment.use_camera()
    except Exception as e:
        assert e.args == ('You must set a camera before trying to use it: call \
            with_parallel_camera or with_perspective_camera first')
