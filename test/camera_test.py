from turtle import circle
from camera import *
from shapes import *
from ray import Ray

def parallel_camera_init_test(np):
    # simple camera basis on y-z plane
    TEST_SIZE = (3, 3)

    u = np.array([0.0, 1.0, 0.0])
    v = np.array([0.0, 0.0, 1.0])
    w = np.array([1.0, 0.0, 0.0])

    e = np.array([0.0, 0.0, 0.0])

    ray_direction = np.array([-1.0, 0.0, 0.0])

    ray_arr = np.empty((3,3), dtype=Ray)
    ray_arr[0] = np.array([Ray(np.array([0.0, -1.0, 1.0]), ray_direction), Ray(np.array([0.0, 0.0, 1.0]), ray_direction), Ray(np.array([0.0, 1.0, 1.0]), ray_direction)])
    ray_arr[1] = np.array([Ray(np.array([0.0, -1.0, 0.0]), ray_direction), Ray(np.array([0.0, 0.0, 0.0]), ray_direction), Ray(np.array([0.0, 1.0, 0.0]), ray_direction)])
    ray_arr[2] = np.array([Ray(np.array([0.0, -1.0, -1.0]), ray_direction), Ray(np.array([0.0, 0.0, -1.0]), ray_direction), Ray(np.array([0.0, 1.0, -1.0]), ray_direction)])

    camera = ParallelCamera(w, v, u, e, TEST_SIZE)

    for i in range(len(ray_arr)):
        for j in range(len(ray_arr[i])):
            assert np.allclose(camera.rays[i,j].origin, ray_arr[i][j].origin) \
                and np.allclose(camera.rays[i,j].direction, ray_arr[i][j].direction), \
                f'''parallel_camera_init_test(valid camera plane)::
                        np.allclose(camera.rays[i,j].origin, ray_arr[i][j].origin): {np.allclose(camera.rays[i,j].origin, ray_arr[i][j].origin)}
                        np.allclose(camera.rays[i,j].direction, ray_arr[i][j].direction): {np.allclose(camera.rays[i,j].direction, ray_arr[i][j].direction)}
                '''

def get_sphere_valid_solution_test(np):
    TEST_SIZE = (1,1)

    u = np.array([0.0, 1.0, 0.0])
    v = np.array([0.0, 0.0, 1.0])
    w = np.array([1.0, 0.0, 0.0])

    e = np.array([0.0, 0.0, 0.0])

    camera = ParallelCamera(w, v, u, e, TEST_SIZE)

    center = np.array([-2.0, 0.0, 0.0])
    radius = 1.2
    color = (0, 0, 0)
    sphere = Sphere(center, radius, color)

    expected_output = 0.8

    actual_output = camera.get_sphere_valid_solution(sphere, camera.rays[0][0])

    assert isclose(actual_output, expected_output)

def get_triangle_valid_solution_test(np):
    pass

def get_solutions_test(np):
    TEST_SIZE = (1,1)

    u = np.array([0.0, 1.0, 0.0])
    v = np.array([0.0, 0.0, 1.0])
    w = np.array([1.0, 0.0, 0.0])

    e = np.array([0.0, 0.0, 0.0])

    camera = ParallelCamera(w, v, u, e, TEST_SIZE)

    center = np.array([-2.0, 0.0, 0.0])
    radius = 1.2
    color = (0, 0, 0)
    sphere = Sphere(center, radius, color)

    expected_output = np.array([0.8])

    actual_output = camera.get_solutions([sphere])

    assert np.allclose(actual_output, expected_output)