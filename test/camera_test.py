from camera import *

def parallel_camera_init_test(np):
    # simple camera basis on y-z plane
    TEST_SIZE = (5, 3)
    u = np.array([0.0, 1.0, 0.0])
    v = np.array([0.0, 0.0, 1.0])
    w = np.array([1.0, 0.0, 0.0])
    e = np.array([0.0, 0.0, 0.0])
    camera = ParallelCamera(w, v, u, e, TEST_SIZE)

    print('parallel_camera_init_test::Camera plane: \n')

    for arr in camera.rays:
            for el in arr:
                print(el.origin, end=' ')
            print()