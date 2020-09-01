from typing import Callable, Dict, Protocol, Tuple, Type, Union, List, Optional

from httpx import Response


class EntityType(Protocol):
    """
    Entity Object Type
    """

    __dataclass_fields__: Dict


Entity = Optional[Union[List[EntityType], EntityType]]
ReturnEntity = Callable[..., Entity]
RequestFunc = Callable[..., Response]
ApiFunc = Callable[..., Tuple[Type[EntityType], Dict]]
