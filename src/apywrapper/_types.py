"""
_types.py
"""


from typing import Callable, Dict, List, Optional, Protocol, Union

from httpx import Response


class EntityType(Protocol):
    # pylint: disable=too-few-public-methods
    """
    Entity Object Type
    """

    __dataclass_fields__: Dict


Entity = Optional[Union[List[EntityType], EntityType]]
ReturnEntity = Callable[..., Entity]
RequestFunc = Callable[..., Response]
ApiFunc = Callable[..., Dict]
