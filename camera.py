class Camera:
    def __init__(self, w, v, u, e):
        return self

    def set_basis(self, w, v, u, e):
        return self

    def take_picture(self):
        pass


class ParallelCamera(Camera):
    def __init__(self, w, v, u, e):
        super().__init__(w, v, u, e)
        return self


class PerspectiveCamera(Camera):
    def __init__(self, w, v, u, e, d):
        super().__init__(w, v, u, e)
        return self

    def set_basis(self, w, v, u, e, d):
        return self