from .abc import ApiMeta
from .path import Path
from .request import HttpClient, make_request


class Api(ApiMeta):
    def __init__(self, host: str, headers) -> None:
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
