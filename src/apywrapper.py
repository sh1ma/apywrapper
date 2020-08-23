from .request import HttpClient
from .abc import ApiMeta
from .path import Path


class Api(ApiMeta):
    def __init__(self, host: str) -> None:
        self.http_client = HttpClient(base_url=host)

    def get(self, path: str):
        def decorator(func):
            def wrapper(*args, **kwargs):
                params = func(*args, **kwargs)
                path_obj = Path(path, params)
                return self.http_client.get_request(path_obj, params)

            return wrapper

        return decorator
