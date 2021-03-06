"""
_types.py
"""


from typing import Any, Callable, Dict, List, Optional, Protocol, Type, Union

from httpx import Response


class PydanticEntityType(Protocol):
    """
    Entity Object Type on Pydantic
    """

    __fields__: Dict


EntityType = PydanticEntityType


Entity = Optional[Union[List[EntityType], EntityType]]
ReturnEntity = Callable[..., Union[Entity, Any]]
RequestFunc = Callable[..., Response]
ApiFunc = Callable[..., Dict]
SerializeFunc = Callable[
    [Type[EntityType], Union[Dict, List]], Union[List[EntityType], EntityType],
]
HookFunc = Callable[[Type[EntityType], Response], Any]
