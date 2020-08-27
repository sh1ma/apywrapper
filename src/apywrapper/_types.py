from typing import Callable, Dict, Protocol, Tuple, Type

from httpx import Response


class EntityType(Protocol):
    """
    Entity Object Type
    """

    __dataclass_fields__: Dict


ReturnEntity = Callable[..., EntityType]
RequestFunc = Callable[..., Response]
ApiFunc = Callable[..., Tuple[Type[EntityType], Dict]]
