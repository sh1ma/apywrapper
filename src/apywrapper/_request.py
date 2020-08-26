from typing import (
    Any,
    Callable,
    Dict,
    Optional,
    Type,
)

from httpx import Client, Response
from dacite import from_dict

from ._path import Path
from ._types import EntityType, ArgsType, KwargsType, ReturnEntity


def serialize(entity: Type[EntityType], response: Response) -> EntityType:
    return from_dict(data_class=entity, data=response.json())


def make_request_function(
    func: Callable[..., Any], *args: ArgsType, **kwargs: KwargsType
) -> Callable[[str, Callable[..., Any]], Any]:
    def wrapper(path_str: str, request_func: Callable[..., Any]):
        entity, params = func(*args, **kwargs)
        path = Path(path_str, params)
        return serialize(entity, request_func(path, params))

    return wrapper


def make_request(
    path_str: str, request_func: Callable[..., Response]
) -> Callable[[Callable[..., Any]], ReturnEntity]:
    def decorator(func: Callable[..., Any]) -> ReturnEntity:
        def wrapper(*args: ArgsType, **kwargs: KwargsType) -> EntityType:
            return make_request_function(func, *args, **kwargs)(path_str, request_func)

        return wrapper

    return decorator


def pick_params(path: Path, params: Optional[Dict]) -> Optional[Dict]:
    if params is None:
        return
    _ = [params.pop(arg) for arg in path.required_args if arg in params]  # type: ignore
    return params


class HttpClient(Client):
    """
    HttpClient
    """

    def get_request(self, path: Path, params: Optional[Dict] = None):
        real_params = pick_params(path, params)
        res = self.get(path, params=real_params)
        res.raise_for_status()
        return res

    def post_request(self, path: Path, params: Optional[Dict] = None):
        params = pick_params(path, params)
        res = self.post(path, json=params)
        res.raise_for_status()
        return res

    def put_request(self, path: Path, params: Optional[Dict] = None):
        params = pick_params(path, params)
        res = self.put(path, json=params)
        res.raise_for_status()
        return res

    def delete_request(self, path: Path, params: Optional[Dict] = None):
        params = pick_params(path, params)
        res = self.delete(path, params=params)
        res.raise_for_status()
        return res

    def patch_request(self, path: Path, params: Optional[Dict] = None):
        params = pick_params(path, params)
        res = self.patch(path, json=params)
        res.raise_for_status()
        return res
