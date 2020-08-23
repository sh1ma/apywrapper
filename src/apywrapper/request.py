import typing
from typing import Callable, List, Union, cast, Any

import httpx
from dacite import from_dict

from .path import Path

T = typing.TypeVar("T")


def make_request(path: str, request_func: Callable) -> Callable[..., Any]:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Union[T, List[T]]:
            entity, params = func(*args, **kwargs)
            path_obj = Path(path, params)
            result = request_func(path_obj, params)
            return cast(Union[T, List[T]], from_dict(data_class=entity, data=result))

        return wrapper

    return decorator


def pick_params(path, params: typing.Dict):
    _ = [params.pop(arg) for arg in path.required_args if arg in params]
    return params


class HttpClient(httpx.Client):
    """
    HttpClient
    """

    def get_request(self, path: Path, params: typing.Dict):
        params = pick_params(path, params)
        res = self.get(path, params=params)
        res.raise_for_status()
        return res.json()

    def post_request(self, path: Path, params: typing.Dict):
        params = pick_params(path, params)
        res = self.post(path, json=params)
        res.raise_for_status()
        return res.json()

    def put_request(self, path: Path, params: typing.Dict):
        params = pick_params(path, params)
        res = self.put(path, json=params)
        res.raise_for_status()
        return res.json()

    def delete_request(self, path: Path, params: typing.Dict):
        params = pick_params(path, params)
        res = self.delete(path, params=params)
        res.raise_for_status()
        return res.json()

    def patch_request(self, path: Path, params: typing.Dict):
        params = pick_params(path, params)
        res = self.patch(path, json=params)
        res.raise_for_status()
        return res.json()
