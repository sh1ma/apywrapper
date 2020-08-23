from src.path import Path
from src.request import pick_params


def test_pick_params():
    @pick_params
    def func(_: Path, params):
        return params

    path = "/articles/{article_id}/comments"
    params = {"article_id": 1234567890, "pages": 1}
    path_obj = Path(path, params)
    assert func(path_obj, params) == {"pages": 1}
