from typing import Dict, Optional, TypeVar, Callable
from .abc import ApiMeta
from .request import HttpClient, make_request


class Api(ApiMeta):
    """
    Api
    """

    def __init__(self, host: str, headers: Optional[Dict] = None) -> None:
        self.http_client = HttpClient(base_url=host, headers=headers)

    def get(self, path: str) -> Callable:
        return make_request(path, self.http_client.get_request)

    def post(self, path: str) -> Callable:
        return make_request(path, self.http_client.post_request)

    def put(self, path: str) -> Callable:
        return make_request(path, self.http_client.put_request)

    def delete(self, path: str) -> Callable:
        return make_request(path, self.http_client.delete_request)

    def patch(self, path: str) -> Callable:
        return make_request(path, self.http_client.patch_request)
