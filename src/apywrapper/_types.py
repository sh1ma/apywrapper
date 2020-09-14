"""
_types.py
"""


from typing import Callable, Dict, List, Optional, Protocol, Type, Union

from httpx import Response


class DataclassEntityType(Protocol):
    # pylint: disable=too-few-public-methods
    """
    Entity Object Type on dataclass
    """

    __dataclass_fields__: Dict


class PydanticEntityType(Protocol):
    """
    Entity Object Type on Pydantic
    """

    __fields__: Dict


EntityType = Union[DataclassEntityType, PydanticEntityType]


Entity = Optional[Union[List[EntityType], EntityType]]
ReturnEntity = Callable[..., Entity]
RequestFunc = Callable[..., Response]
ApiFunc = Callable[..., Dict]
SerializeFunc = Callable[
    [Type[EntityType], Union[Dict, List]], Union[List[EntityType], EntityType],
]
