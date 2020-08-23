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
        res.raise_for_status()
        return res

    def post_request(self, path: Path, params: typing.Dict):
        params = pick_params(path, params)
        res = self.post(path, params=params)
        res.raise_for_status()
        return res

    def put_request(self, path: Path, params: typing.Dict):
        params = pick_params(path, params)
        res = self.put(path, params=params)
        res.raise_for_status()
        return res

    def delete_request(self, path: Path, params: typing.Dict):
        params = pick_params(path, params)
        res = self.delete(path, params=params)
        res.raise_for_status()
        return res

    def patch_request(self, path: Path, params: typing.Dict):
        params = pick_params(path, params)
        res = self.patch(path, params=params)
        res.raise_for_status()
        return res
