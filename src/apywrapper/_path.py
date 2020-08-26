from ._types import ParamsType
import string


formatter = string.Formatter()


class Path(str):
    """
    Path
    """

    def __new__(cls, path: str, params: ParamsType) -> str:
        formatted = path.format(**params)
        path = super().__new__(cls, formatted)  # type: ignore
        return path

    def __init__(self, path: str, params: ParamsType):
        # pylint: disable=super-init-not-called, unused-argument
        self.required_args = [e[1] for e in formatter.parse(path)]
