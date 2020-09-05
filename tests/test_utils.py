from typing import Dict, List

import pytest

from apywrapper._utils import get_returntype_from_annotation


def test_get_returntype_from_annotation():
    def test1() -> List[str]:
        pass

    def test2() -> Dict[str, str]:
        pass

    def test3() -> None:
        pass

    assert get_returntype_from_annotation(test1) is str
    with pytest.raises(Exception):
        get_returntype_from_annotation(test2)
    assert get_returntype_from_annotation(test3) is None
