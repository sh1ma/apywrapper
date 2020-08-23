from abc import ABCMeta


class ApiMeta(metaclass=ABCMeta):
    """
    ApiMeta
    """

    def get(self, path: str):
        raise NotImplementedError

    def post(self, path: str):
        raise NotImplementedError

    def put(self, path: str):
        raise NotImplementedError

    def delete(self, path: str):
        raise NotImplementedError

    def patch(self, path: str):
        raise NotImplementedError
