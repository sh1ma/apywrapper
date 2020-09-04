from inspect import signature
from typing import List


def get_returntype_from_annotation(func):
    return_annotation = signature(func).return_annotation
    if hasattr(return_annotation, "__origin__"):
        if return_annotation.__origin__ is not list:
            raise Exception(
                f"type must be List[Entity] or Entity, not {return_annotation}"
            )
        return return_annotation.__args__[0]
    return return_annotation
