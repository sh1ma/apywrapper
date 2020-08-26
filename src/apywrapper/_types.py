from typing import (
    Protocol,
    Optional,
    Union,
    Iterator,
    Dict,
    Sequence,
    Tuple,
    Mapping,
    List,
    TypeVar,
)
from ._path import Path

T = TypeVar("T")


class EntityType(Protocol):
    """
    Entity Object Type
    """

    __dataclass_fields__: Dict


PrimitiveDataType = Union[str, int, float, bool]

PathType = Union[Path, str]

HeaderType = Union[
    Dict[str, str], Dict[bytes, bytes],
]

RequestDataType = Mapping[str, Union[dict, str, bytes, Iterator[bytes]]]
QueryParamsType = Optional[
    Dict[
        Mapping[str, Union[PrimitiveDataType, Sequence[PrimitiveDataType]]],
        List[Tuple[str, PrimitiveDataType]],
    ]
]

ParamsType = Union[RequestDataType, QueryParamsType]
