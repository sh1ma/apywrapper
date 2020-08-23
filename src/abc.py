from abc import ABCMeta


class ApiMeta(metaclass=ABCMeta):
    def get(self, path: str):
        raise NotImplementedError
