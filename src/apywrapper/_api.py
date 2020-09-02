from httpx._types import HeaderTypes

from ._abc import Api
from ._request import HttpClient, make_request


def get(path):
    def _get(func):
        def wrapper(self, *args, **kwargs):
            return make_request(path, self.http_client.get_request)(func)(
                self, *args, **kwargs
            )

        return wrapper

    return _get


def post(path):
    def _post(func):
        def wrapper(self, *args, **kwargs):
            return make_request(path, self.http_client.post_request)(func)(
                self, *args, **kwargs
            )

        return wrapper

    return _post


def put(path):
    def _put(func):
        def wrapper(self, *args, **kwargs):
            return make_request(path, self.http_client.put_request)(func)(
                self, *args, **kwargs
            )

        return wrapper

    return _put


def delete(path):
    def _delete(func):
        def wrapper(self, *args, **kwargs):
            return make_request(path, self.http_client.delete_request)(func)(
                self, *args, **kwargs
            )

        return wrapper

    return _delete


def patch(path):
    def _patch(func):
        def wrapper(self, *args, **kwargs):
            return make_request(path, self.http_client.patch_request)(func)(
                self, *args, **kwargs
            )

        return wrapper

    return _patch


class Apy(Api):
    """
    Apy class
    """

    def __init__(self, host: str, headers: HeaderTypes) -> None:
        self.http_client = HttpClient(base_url=host, headers=headers)

    def get(self, path: str):
        return make_request(path, self.http_client.get_request)

    def post(self, path: str):
        return make_request(path, self.http_client.post_request)

    def put(self, path: str):
        return make_request(path, self.http_client.put_request)

    def delete(self, path: str):
        return make_request(path, self.http_client.delete_request)

    def patch(self, path: str):
        return make_request(path, self.http_client.patch_request)
