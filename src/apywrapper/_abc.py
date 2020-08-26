from typing import Callable, Any, TypeVar
from ._types import EntityType
from abc import ABCMeta


ArgsType = TypeVar("ArgsType")
KwargsType = TypeVar("KwargsType")


class Api(metaclass=ABCMeta):
    """
    ApiMeta
    """

    def get(
        self, path: str
    ) -> Callable[[Callable[..., Any]], Callable[[ArgsType, KwargsType], EntityType]]:
        raise NotImplementedError

    def post(
        self, path: str
    ) -> Callable[[Callable[..., Any]], Callable[[ArgsType, KwargsType], EntityType]]:
        raise NotImplementedError

    def put(
        self, path: str
    ) -> Callable[[Callable[..., Any]], Callable[[ArgsType, KwargsType], EntityType]]:
        raise NotImplementedError

    def delete(
        self, path: str
    ) -> Callable[[Callable[..., Any]], Callable[[ArgsType, KwargsType], EntityType]]:
        raise NotImplementedError

    def patch(
        self, path: str
    ) -> Callable[[Callable[..., Any]], Callable[[ArgsType, KwargsType], EntityType]]:
        raise NotImplementedError
