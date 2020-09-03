"""
_abc.py
"""

from abc import ABCMeta
from typing import Callable

from ._types import ApiFunc, ReturnEntity


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
