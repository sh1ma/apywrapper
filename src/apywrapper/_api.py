"""
_api.py
"""

from typing import Any, Callable, Optional

from httpx._types import HeaderTypes

from ._abc import Api
from ._request import HttpClient, make_request, make_request_function
from ._types import ApiFunc, Entity, HookFunc, ReturnEntity, SerializeFunc


class Apy(Api):
    """
    Apy class
    """

    def __init__(
        self,
        host: str,
        headers: HeaderTypes,
        hook_func: Optional[HookFunc] = None,
        serialize_func: Optional[SerializeFunc] = None,
    ) -> None:
        self.hook_func = hook_func if hook_func else None
        self.serialize_func = serialize_func if serialize_func else None
        self.http_client = HttpClient(base_url=host, headers=headers)

    def get(self, path: str) -> Callable[[ApiFunc], ReturnEntity]:
        return make_request(
            path, self.http_client.get_request, self.hook_func, self.serialize_func
        )

    def post(self, path: str) -> Callable[[ApiFunc], ReturnEntity]:
        return make_request(
            path, self.http_client.post_request, self.hook_func, self.serialize_func
        )

    def put(self, path: str) -> Callable[[ApiFunc], ReturnEntity]:
        return make_request(
            path, self.http_client.put_request, self.hook_func, self.serialize_func
        )

    def delete(self, path: str) -> Callable[[ApiFunc], ReturnEntity]:
        return make_request(
            path, self.http_client.delete_request, self.hook_func, self.serialize_func
        )

    def patch(self, path: str) -> Callable[[ApiFunc], ReturnEntity]:
        return make_request(
            path, self.http_client.patch_request, self.hook_func, self.serialize_func
        )


def get(path: str) -> Callable[[ApiFunc], ReturnEntity]:
    def _get(func: ApiFunc) -> ReturnEntity:
        def wrapper(self: Apy, *args: Any, **kwargs: Any) -> Entity:
            return make_request_function(func, self, *args, **kwargs)(
                path, self.http_client.get_request, self.hook_func, self.serialize_func
            )

        return wrapper

    return _get


def post(path: str) -> Callable[[ApiFunc], ReturnEntity]:
    def _post(func: ApiFunc) -> ReturnEntity:
        def wrapper(self: Apy, *args: Any, **kwargs: Any) -> Entity:
            return make_request_function(func, self, *args, **kwargs)(
                path, self.http_client.post_request, self.hook_func, self.serialize_func
            )

        return wrapper

    return _post


def put(path: str) -> Callable[[ApiFunc], ReturnEntity]:
    def _put(func: ApiFunc) -> ReturnEntity:
        def wrapper(self: Apy, *args: Any, **kwargs: Any) -> Entity:
            return make_request_function(func, self, *args, **kwargs)(
                path, self.http_client.put_request, self.hook_func, self.serialize_func
            )

        return wrapper

    return _put


def delete(path: str) -> Callable[[ApiFunc], ReturnEntity]:
    def _delete(func: ApiFunc) -> ReturnEntity:
        def wrapper(self: Apy, *args: Any, **kwargs: Any) -> Entity:
            return make_request_function(func, self, *args, **kwargs)(
                path,
                self.http_client.delete_request,
                self.hook_func,
                self.serialize_func,
            )

        return wrapper

    return _delete


def patch(path: str) -> Callable[[ApiFunc], ReturnEntity]:
    def _patch(func: ApiFunc) -> ReturnEntity:
        def wrapper(self: Apy, *args: Any, **kwargs: Any) -> Entity:
            return make_request_function(func, self, *args, **kwargs)(
                path,
                self.http_client.patch_request,
                self.hook_func,
                self.serialize_func,
            )

        return wrapper

    return _patch
