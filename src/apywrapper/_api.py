from httpx._types import HeaderTypes

from ._abc import Api
from ._request import HttpClient, make_request


def get(path):
    def _get(func):
        def wrapper(self, *args):
            return make_request(path, self.http_client.get_request)(func)(self, *args)

        return wrapper

    return _get


def post(path):
    def _post(func):
        def wrapper(self, *args):
            return make_request(path, self.http_client.post_request)(func)(self, *args)

        return wrapper

    return _post


def put(path):
    def _put(func):
        def wrapper(self, *args):
            return make_request(path, self.http_client.put_request)(func)(self, *args)

        return wrapper

    return _put


def delete(path):
    def _delete(func):
        def wrapper(self, *args):
            return make_request(path, self.http_client.delete_request)(func)(
                self, *args
            )

        return wrapper

    return _delete


def patch(path):
    def _patch(func):
        def wrapper(self, *args):
            return make_request(path, self.http_client.patch_request)(func)(self, *args)

        return wrapper

    return _patch


class Apy(Api):
    """
    Apy class
    """

    def __init__(self, host: str, headers: HeaderTypes) -> None:
        self.http_client = HttpClient(base_url=host, headers=headers)

    def get(self, path: str, request_func=None):
        request_func = (
            request_func if request_func is not None else self.http_client.get_request
        )
        return make_request(path, request_func)

    def post(self, path: str, request_func=None):
        request_func = (
            request_func if request_func is not None else self.http_client.post_request
        )
        return make_request(path, request_func)

    def put(self, path: str, request_func=None):
        request_func = (
            request_func if request_func is not None else self.http_client.put_request
        )
        return make_request(path, request_func)

    def delete(self, path: str, request_func=None):
        request_func = (
            request_func
            if request_func is not None
            else self.http_client.delete_request
        )
        return make_request(path, request_func)

    def patch(self, path: str, request_func=None):
        request_func = (
            request_func if request_func is not None else self.http_client.patch_request
        )
        return make_request(path, request_func)
