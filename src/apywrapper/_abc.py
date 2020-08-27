from typing import Callable, Any, TypeVar
from ._types import ApiFunc, ReturnEntity
from abc import ABCMeta


ArgsType = TypeVar("ArgsType")
KwargsType = TypeVar("KwargsType")


class Api(metaclass=ABCMeta):
    """
    ApiMeta
    """

    def get(self, path: str) -> Callable[[ApiFunc], ReturnEntity]:
        raise NotImplementedError

    def post(self, path: str) -> Callable[[ApiFunc], ReturnEntity]:
        raise NotImplementedError

    def put(self, path: str) -> Callable[[ApiFunc], ReturnEntity]:
        raise NotImplementedError

    def delete(self, path: str) -> Callable[[ApiFunc], ReturnEntity]:
        raise NotImplementedError

    def patch(self, path: str) -> Callable[[ApiFunc], ReturnEntity]:
        raise NotImplementedError
