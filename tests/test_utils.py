from typing import Dict, List, Union

import pytest

from apywrapper._utils import get_returntype_from_annotation


def test_get_returntype_from_annotation():
    def test1() -> List[str]:
        pass

    def test2() -> Dict[str, str]:
        pass

    def test3() -> None:
        pass

    def test4() -> List[List[Union[str, int]]]:
        pass

    assert get_returntype_from_annotation(test1) is str
    assert get_returntype_from_annotation(test2) is dict
    assert get_returntype_from_annotation(test3) is None
    assert get_returntype_from_annotation(test4) is Union
