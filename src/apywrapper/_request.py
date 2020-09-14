"""
_request.py
"""


from typing import Any, Callable, Dict, List, Optional, Type, Union, cast

from dacite import from_dict
from httpx import Client, Response

from ._path import Path
from ._types import (
    ApiFunc,
    Entity,
    EntityType,
    RequestFunc,
    ReturnEntity,
    SerializeFunc,
)
from ._utils import get_returntype_from_annotation


def serialize(
    entity: Type[EntityType], json: Union[Dict, List]
) -> Union[List[EntityType], EntityType]:
    if isinstance(json, list):
        return [cast(EntityType, from_dict(data_class=entity, data=d)) for d in json]

    return cast(EntityType, from_dict(data_class=entity, data=json))


def make_request_function(
    func: ApiFunc, *args: Any, **kwargs: Any
) -> Callable[[str, RequestFunc, Optional[SerializeFunc]], Entity]:
    def wrapper(
        path_str: str,
        request_func: RequestFunc,
        serialize_func: Optional[SerializeFunc] = None,
    ) -> Entity:
        entity = get_returntype_from_annotation(func)
        params = func(*args, **kwargs)
        path = Path(path_str, params)
        response = request_func(path, params)
        if (
            entity is None or response.status_code == 204
        ):  # entity is None or response body is None
            return None
        if serialize_func:
            return serialize_func(entity, response.json())
        return serialize(entity, response.json())

    return wrapper


def make_request(
    path_str: str,
    request_func: RequestFunc,
    serialize_func: Optional[SerializeFunc] = None,
) -> Callable[[ApiFunc], ReturnEntity]:
    def decorator(func: ApiFunc) -> ReturnEntity:
        def wrapper(*args: Any, **kwargs: Any) -> Entity:
            return make_request_function(func, *args, **kwargs)(
                path_str, request_func, serialize_func
            )

        return wrapper

    return decorator


def pick_params(path: Path, params: Optional[Dict]) -> Optional[Dict]:
    if params is None:
        return None
    _ = [params.pop(arg) for arg in path.required_args if arg in params]
    return params


class HttpClient(Client):
    """
    HttpClient
    """

    def get_request(self, path: Path, params: Optional[Dict] = None) -> Response:
        real_params = pick_params(path, params)
        res = self.get(path, params=real_params)
        res.raise_for_status()
        return res

    def post_request(self, path: Path, params: Optional[Dict] = None) -> Response:
        params = pick_params(path, params)
        res = self.post(path, json=params)
        res.raise_for_status()
        return res

    def put_request(self, path: Path, params: Optional[Dict] = None) -> Response:
        params = pick_params(path, params)
        res = self.put(path, json=params)
        res.raise_for_status()
        return res

    def delete_request(self, path: Path, params: Optional[Dict] = None) -> Response:
        params = pick_params(path, params)
        res = self.delete(path, params=params)
        res.raise_for_status()
        return res

    def patch_request(self, path: Path, params: Optional[Dict] = None) -> Response:
        params = pick_params(path, params)
        res = self.patch(path, json=params)
        res.raise_for_status()
        return res
