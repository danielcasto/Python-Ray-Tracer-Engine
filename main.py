import pygame as pg
import numpy as np
from environment import Environment
from sys import exit

SCREEN_DIMENSIONS = (1000, 600) # (width, height)

def display_test():
    pg.init()

    test_surf = pg.Surface(SCREEN_DIMENSIONS)
    TEST_RGB = np.full((1000, 600, 3), (255,0,0))

    screen = pg.display.set_mode(SCREEN_DIMENSIONS, pg.RESIZABLE)
    pg.display.set_caption('DISPLAY TEST')
    program_is_alive = True
    
    pg.surfarray.blit_array(test_surf, TEST_RGB)

    # game loop
    while program_is_alive:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                program_is_alive = False

        screen.blit(test_surf, (0,0))
        pg.display.flip()
        
    pg.quit()
    exit()

def main():
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
    # display_test()