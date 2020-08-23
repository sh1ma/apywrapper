from functools import partial, partialmethod

from .request import HttpClient
from .abc import ApiMeta
from .path import Path


def make_request(path: str, request_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            params = func(*args, **kwargs)
            path_obj = Path(path, params)
            return request_func(path_obj, params)

        return wrapper

    return decorator


class Api(ApiMeta):
    def __init__(self, host: str) -> None:
        self.http_client = HttpClient(base_url=host)

    def get(self, path):
        return make_request(path, self.http_client.get_request)

    def post(self, path):
        return make_request(path, self.http_client.post_request)

    def put(self, path):
        return make_request(path, self.http_client.put_request)

    def delete(self, path):
        return make_request(path, self.http_client.delete_request)

    def patch(self, path):
        return make_request(path, self.http_client.patch_request)
