from camera import *
from ray import Ray

def parallel_camera_init_test(np):
    # simple camera basis on y-z plane
    TEST_SIZE = (3, 3)

    u = np.array([0.0, 1.0, 0.0])
    v = np.array([0.0, 0.0, 1.0])
    w = np.array([1.0, 0.0, 0.0])
    e = np.array([0.0, 0.0, 0.0])

    ray_direction = np.array([-1.0, 0.0, 0.0])

    ray_arr = []
    ray_arr.append([Ray(np.array([0.0, -1.0, 1.0]), ray_direction), Ray(np.array([0.0, 0.0, 1.0]), ray_direction), Ray(np.array([0.0, 1.0, 1.0]), ray_direction)])
    ray_arr.append([Ray(np.array([0.0, -1.0, 0.0]), ray_direction), Ray(np.array([0.0, 0.0, 0.0]), ray_direction), Ray(np.array([0.0, 1.0, 0.0]), ray_direction)])
    ray_arr.append([Ray(np.array([0.0, -1.0, -1.0]), ray_direction), Ray(np.array([0.0, 0.0, -1.0]), ray_direction), Ray(np.array([0.0, 1.0, -1.0]), ray_direction)])

    camera = ParallelCamera(w, v, u, e, TEST_SIZE)

    for i in range(len(ray_arr)):
        for j in range(len(ray_arr[i])):
            assert np.allclose(camera.rays[i][j].origin, ray_arr[i][j].origin) \
                and np.allclose(camera.rays[i][j].direction, ray_arr[i][j].direction), \
                f'''parallel_camera_init_test(valid camera plane)::
                        np.allclose(camera.rays[i][j].origin, ray_arr[i][j].origin): {np.allclose(camera.rays[i][j].origin, ray_arr[i][j].origin)}
                        np.allclose(camera.rays[i][j].direction, ray_arr[i][j].direction): {np.allclose(camera.rays[i][j].direction, ray_arr[i][j].direction)}
                '''