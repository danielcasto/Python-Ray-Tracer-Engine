from io import UnsupportedOperation

class Camera:
    def __init__(self, w, v, u, e):
        # TODO currently unsupported
        raise UnsupportedOperation
        return self

    def set_basis(self, w, v, u, e):
        # TODO currently unsupported
        raise UnsupportedOperation
        return self

    def take_picture(self):
        # TODO currently unsupported
        raise UnsupportedOperation
        pass


class ParallelCamera(Camera):
    def __init__(self, w, v, u, e):
        super().__init__(w, v, u, e)
        # TODO currently unsupported
        raise UnsupportedOperation
        return self


class PerspectiveCamera(Camera):
    def __init__(self, w, v, u, e, d):
        super().__init__(w, v, u, e)
        # TODO currently unsupported
        raise UnsupportedOperation
        return self

    def set_basis(self, w, v, u, e, d):
        # TODO currently unsupported
        raise UnsupportedOperation
        return self