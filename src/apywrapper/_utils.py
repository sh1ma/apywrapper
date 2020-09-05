"""
_utils.py
"""

from inspect import signature
from typing import Optional, Type, cast

from ._types import ApiFunc, EntityType


def get_returntype_from_annotation(func: ApiFunc) -> Optional[Type[EntityType]]:
    return_annotation = signature(func).return_annotation
    if return_annotation is None:
        return None
    if hasattr(return_annotation, "__origin__"):
        if return_annotation.__origin__ is not list:
            raise Exception(f"return type must be Entity, not {return_annotation}")
        return cast(Type[EntityType], return_annotation.__args__[0])
    return cast(Type[EntityType], return_annotation)
