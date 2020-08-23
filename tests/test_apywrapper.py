# from dataclasses import dataclass

# import pytest
# from dataclasses_json import DataClassJsonMixin

# from src.abc import ApiMeta
# from src.path import Path
# from src.request import pick_params


# class ResponseMock:
#     @staticmethod
#     def json():
#         return {"user_id": 1, "name": "sh1ma", "age": 20}


# @dataclass
# class UserMock(DataClassJsonMixin):
#     user_id: int
#     name: str
#     age: int


# class HttpClientMock:
#     def __init__(self, host: str):
#         self.base_url = host

#     @pick_params
#     def get_request(self, path, params):
#         if params["name"] == "sh1ma":
#             return ResponseMock.json()


# class ApiTestable(ApiMeta):
#     def __init__(self, host: str) -> None:
#         self.http_client = HttpClientMock(host)

#     def get(self, path: str):
#         def decorator(func):
#             def wrapper(*args, **kwargs):
#                 entity, params = func(*args, **kwargs)
#                 path_obj = Path(path, params)
#                 return self.http_client.get_request(path_obj, params)

#             return wrapper

#         return decorator


# @pytest.fixture
# def init_api():
#     api = ApiTestable("http://api.example.com")
#     return api


# def test_get(api):
#     @api.get("/users/{user_id}")
#     def get_user(user_id: int):
#         return UserMock, {"user_id": user_id}

#     assert get_user(1) == UserMock(1, "sh1ma", 20)
