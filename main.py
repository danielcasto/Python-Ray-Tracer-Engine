import pygame as pg
import numpy as np
from environment import Environment
from sys import exit, argv
from test.camera_test import *
from test.environment_test import *
from test.display_test import *

SCREEN_DIMENSIONS = (1025, 511) # (width, height)
# TODO for now only odd dimensions are supported

def run_tests():
    print('\n\nRunning tests...\n\n')
    
    # camera tests
    #parallel_camera_init_test(np)
    #get_sphere_valid_solution_test(np)
    get_solutions_test(np)

    # environnment tests
    '''environment_init_test()
    add_light_sources_test(np)
    add_triangle_test(np)
    add_sphere_test(np)
    with_parallel_camera_test(np)
    with_perspective_camera_test(np)
    use_camera_test(np)

    display_test(pg, np, SCREEN_DIMENSIONS, exit)'''

def main():
    # Check for test command line arg

    if len(argv) == 2 and argv[1] == 'test':
        run_tests()
        return

    pg.init()
    screen = pg.display.set_mode(SCREEN_DIMENSIONS, pg.RESIZABLE)
    pg.display.set_caption('Python Ray Tracer Engine')
    program_is_alive = True
    surf = pg.Surface(SCREEN_DIMENSIONS)

    env = Environment(SCREEN_DIMENSIONS)

    rgb_arr = env.use_camera()
    
    pg.surfarray.blit_array(surf, rgb_arr)

    # game loop
    while program_is_alive:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                program_is_alive = False

        screen.blit(surf, (0,0))
        pg.display.flip()
        
    pg.quit()
    exit()     

if __name__ == '__main__':
    main()