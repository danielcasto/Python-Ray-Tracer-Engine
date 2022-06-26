from time import sleep


def display_test(pg, np, SCREEN_DIMENSIONS, exit):
    pg.init()

    test_surf = pg.Surface(SCREEN_DIMENSIONS)
    TEST_RGB = np.full((1000, 600, 3), (255,0,0))

    screen = pg.display.set_mode(SCREEN_DIMENSIONS, pg.RESIZABLE)
    pg.display.set_caption('DISPLAY TEST')
    program_is_alive = True
    
    pg.surfarray.blit_array(test_surf, TEST_RGB)

    screen.blit(test_surf, (0,0))
    pg.display.flip()

    sleep(0.5)

    pg.quit()
    exit()