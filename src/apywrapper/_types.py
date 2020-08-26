from typing import Protocol, Dict, TypeVar, Callable


class EntityType(Protocol):
    """
    Entity Object Type
    """

    __dataclass_fields__: Dict


ArgsType = TypeVar("ArgsType")
KwargsType = TypeVar("KwargsType")

ReturnEntity = Callable[[ArgsType, KwargsType], EntityType]
