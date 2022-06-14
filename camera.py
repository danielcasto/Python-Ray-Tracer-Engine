class Camera:
    def __init__(self, w, v, u, e):
        # TODO
        return self

    def set_basis(self, w, v, u, e):
        # TODO
        return self

    def take_picture(self):
        # TODO
        pass


class ParallelCamera(Camera):
    def __init__(self, w, v, u, e):
        super().__init__(w, v, u, e)
        # TODO
        return self


class PerspectiveCamera(Camera):
    def __init__(self, w, v, u, e, d):
        super().__init__(w, v, u, e)
        # TODO
        return self

    def set_basis(self, w, v, u, e, d):
        # TODO
        return self