"""
_path.py
"""

import string
from typing import Dict

formatter = string.Formatter()


class Path(str):
    """
    Path
    """

    def __new__(cls, path: str, params: Dict) -> str:  # type: ignore
        formatted = path.format(**params)
        path = super().__new__(cls, formatted)  # type: ignore
        return path

    def __init__(self, path: str, params: Dict):
        # pylint: disable=super-init-not-called, unused-argument
        self.required_args = [e[1] for e in formatter.parse(path)]
