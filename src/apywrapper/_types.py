from typing import (
    Protocol,
    Dict,
    TypeVar,
)

T = TypeVar("T")


class EntityType(Protocol):
    """
    Entity Object Type
    """

    __dataclass_fields__: Dict


ArgsType = TypeVar("ArgsType")
KwargsType = TypeVar("KwargsType")
