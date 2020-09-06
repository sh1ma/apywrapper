"""
_utils.py
"""

from inspect import signature
from typing import Any, Optional, Type, cast, get_args, get_origin

from ._types import ApiFunc, EntityType


def get_returntype_from_annotation(func: ApiFunc) -> Optional[Type[EntityType]]:
    return_annotation = signature(func).return_annotation
    if return_annotation is None:
        return None
    return resolve_returntype(return_annotation)


def resolve_returntype(tp: Any) -> Type[EntityType]:
    if (tp_origin := get_origin(tp)) is not None:
        if tp_origin is not list:
            return get_origin(tp)
        return cast(Type[EntityType], resolve_returntype(get_args(tp)[0]))
