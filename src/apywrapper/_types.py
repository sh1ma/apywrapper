from httpx import Response
from httpx._types import PrimitiveData
from typing import Protocol, Dict, TypeVar, Callable, Tuple, Type


class EntityType(Protocol):
    """
    Entity Object Type
    """

    __dataclass_fields__: Dict


ReturnEntity = Callable[..., EntityType]
RequestFunc = Callable[..., Response]
ApiFunc = Callable[..., Tuple[Type[EntityType], Dict]]
