"""
_utils.py
"""

from inspect import signature
from typing import Any

from ._types import ApiFunc


def get_returntype_from_annotation(func: ApiFunc) -> Any:
    return_annotation = signature(func).return_annotation
    return return_annotation


# def resolve_returntype(tp: Any) -> Type[EntityType]:
#     if (tp_origin := get_origin(tp)) is not None:
#         if tp_origin is not list:
#             return cast(Type[EntityType], get_origin(tp))
#         return resolve_returntype(get_args(tp)[0])
#     return cast(Type[EntityType], tp)
