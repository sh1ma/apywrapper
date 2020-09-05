"""
_api.py
"""

from typing import Any, Callable

from httpx._types import HeaderTypes

from ._abc import Api
from ._request import HttpClient, make_request, make_request_function
from ._types import ApiFunc, Entity, ReturnEntity


class Apy(Api):
    """
    Apy class
    """

    def __init__(self, host: str, headers: HeaderTypes) -> None:
        self.http_client = HttpClient(base_url=host, headers=headers)

    def get(self, path: str) -> Callable[[ApiFunc], ReturnEntity]:
        return make_request(path, self.http_client.get_request)

    def post(self, path: str) -> Callable[[ApiFunc], ReturnEntity]:
        return make_request(path, self.http_client.post_request)

    def put(self, path: str) -> Callable[[ApiFunc], ReturnEntity]:
        return make_request(path, self.http_client.put_request)

    def delete(self, path: str) -> Callable[[ApiFunc], ReturnEntity]:
        return make_request(path, self.http_client.delete_request)

    def patch(self, path: str) -> Callable[[ApiFunc], ReturnEntity]:
        return make_request(path, self.http_client.patch_request)


def get(path: str) -> Callable[[ApiFunc], ReturnEntity]:
    def _get(func: ApiFunc) -> ReturnEntity:
        def wrapper(self: Apy, *args: Any, **kwargs: Any) -> Entity:
            return make_request_function(func, self, *args, **kwargs)(
                path, self.http_client.get_request
            )

        return wrapper

    return _get


def post(path: str) -> Callable[[ApiFunc], ReturnEntity]:
    def _post(func: ApiFunc) -> ReturnEntity:
        def wrapper(self: Apy, *args: Any, **kwargs: Any) -> Entity:
            return make_request_function(func, self, *args, **kwargs)(
                path, self.http_client.post_request
            )

        return wrapper

    return _post


def put(path: str) -> Callable[[ApiFunc], ReturnEntity]:
    def _put(func: ApiFunc) -> ReturnEntity:
        def wrapper(self: Apy, *args: Any, **kwargs: Any) -> Entity:
            return make_request_function(func, self, *args, **kwargs)(
                path, self.http_client.put_request
            )

        return wrapper

    return _put


def delete(path: str) -> Callable[[ApiFunc], ReturnEntity]:
    def _delete(func: ApiFunc) -> ReturnEntity:
        def wrapper(self: Apy, *args: Any, **kwargs: Any) -> Entity:
            return make_request_function(func, self, *args, **kwargs)(
                path, self.http_client.delete_request
            )

        return wrapper

    return _delete


def patch(path: str) -> Callable[[ApiFunc], ReturnEntity]:
    def _patch(func: ApiFunc) -> ReturnEntity:
        def wrapper(self: Apy, *args: Any, **kwargs: Any) -> Entity:
            return make_request_function(func, self, *args, **kwargs)(
                path, self.http_client.patch_request
            )

        return wrapper

    return _patch
