from apywrapper._path import Path


def test_Path():
    text = "/users/{user_id}"
    params = {"user_id": "sh1ma"}
    path = Path(text, params)
    assert path == "/users/sh1ma"
    assert path.required_args == ["user_id"]
