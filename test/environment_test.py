from environment import Environment

def env_init_test():
    TEST_SIZE = (500, 500)
    env = Environment(TEST_SIZE)

    assert env.size == TEST_SIZE