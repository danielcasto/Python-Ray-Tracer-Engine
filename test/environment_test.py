from environment import Environment

def environment_init_test():
    TEST_SIZE = (500, 500)
    environment = Environment(TEST_SIZE)

    assert environment.size == TEST_SIZE, f"environment_init_test: TEST_SIZE: {TEST_SIZE}, is not equal to env.size: {environment.size}"



