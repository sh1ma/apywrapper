import typing
import httpx

from .path import Path


def pick_params(path, params: typing.Dict):
    _ = [params.pop(arg) for arg in path.required_args if arg in params]
    return params


class HttpClient(httpx.Client):
    def get_request(self, path: Path, params: typing.Dict):
        params = pick_params(path, params)
        res = self.get(path, params=params)
        return res
