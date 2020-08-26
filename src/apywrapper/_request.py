import typing
from typing import (
    Any,
    AnyStr,
    Callable,
    Dict,
    Iterator,
    List,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
)

import httpx
from dacite import from_dict

from ._path import Path
from ._types import EntityType, HeaderType

ArgsType = TypeVar("ArgsType")
KwargsType = TypeVar("KwargsType")
Params = Union[dict, str, bytes, Iterator[bytes]]

# Params = Optional[typing.Dict["str", RequestData]]


# def make_request(
#     path: str, request_func: Callable[..., Any]
# ) -> Callable[[Callable], Callable]:
#     def decorator(func: Callable) -> Callable:
#         def wrapper(*args, **kwargs) -> Union[T, List[T]]:
#             entity, params = func(*args, **kwargs)
#             path_obj = Path(path, params)
#             result = request_func(path_obj, params)
#             return cast(Union[T, List[T]], from_dict(data_class=entity, data=result))

#         return wrapper

#     return decorator


# def prepare_request(
#     path_str: str, func: Callable[..., Any], *args: ArgsType, **kwargs: KwargsType
# ) -> Tuple[EntityType, Dict[str, Any], Path]:
#     entity, params = func(*args, *kwargs)
#     path = Path(path_str, params)
#     return entity, params, path

# def c(entity: EntityType, response: httpx.):


def c(entity: Type[EntityType], response: httpx.Response) -> EntityType:
    return from_dict(data_class=entity, data=response.json())
    # return


def b(
    func: Callable[..., Any], *args: ArgsType, **kwargs: KwargsType
) -> Callable[[str, Callable[..., Any]], Any]:
    def wrapper(path_str: str, request_func: Callable[..., Any]):
        entity, params = func(*args, **kwargs)
        path = Path(path_str, params)
        return c(entity, request_func(path, params))

    return wrapper


def make_request(
    path_str: str, request_func: Callable[..., httpx.Response]
) -> Callable[[Callable[..., Any]], Callable[[ArgsType, KwargsType], EntityType]]:
    def decorator(
        func: Callable[..., Any]
    ) -> Callable[[ArgsType, KwargsType], EntityType]:
        def wrapper(*args: ArgsType, **kwargs: KwargsType) -> EntityType:
            return b(func, *args, **kwargs)(path_str, request_func)

        return wrapper

    return decorator


# def serialize(entity: Type[EntityType], json: Any) -> EntityType:
#     return from_dict(data_class=entity, data=json)


# def make_request(entity: Type[EntityType], params, path) -> EntityType:
#     return entity()


def pick_params(
    path: Path, params: Optional[typing.Dict["str", Params]] = None
) -> Optional[Params]:
    if params is None:
        return
    _ = [params.pop(arg) for arg in path.required_args if arg in params]  # type: ignore
    return params


class HttpClient(httpx.Client):
    """
    HttpClient
    """

    def get_request(
        self, path: Path, params: Optional[typing.Dict["str", Params]] = None
    ):
        params = pick_params(path, params)
        res = self.get(path, params=params)
        res.raise_for_status()
        return res

    def post_request(self, path: Path, params: typing.Dict):
        params = pick_params(path, params)
        res = self.post(path, json=params)
        res.raise_for_status()
        return res

    def put_request(self, path: Path, params: typing.Dict):
        params = pick_params(path, params)
        res = self.put(path, json=params)
        res.raise_for_status()
        return res

    def delete_request(self, path: Path, params: typing.Dict):
        params = pick_params(path, params)
        res = self.delete(path, params=params)
        res.raise_for_status()
        return res

    def patch_request(self, path: Path, params: typing.Dict):
        params = pick_params(path, params)
        res = self.patch(path, json=params)
        res.raise_for_status()
        return res
