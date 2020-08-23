from src.path import Path
from src.request import pick_params


def test_pick_params():
    path = "/articles/{article_id}/comments"
    params = {"article_id": 1234567890, "pages": 1}
    path_obj = Path(path, params)
    assert pick_params(path_obj, params) == {"pages": 1}
