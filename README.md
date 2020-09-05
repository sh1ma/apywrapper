## apywrapper

![lint](https://github.com/sh1ma/apywrapper/workflows/lint/badge.svg?branch=develop)
[![PyPI version](https://badge.fury.io/py/apywrapper.svg)](https://badge.fury.io/py/apywrapper)

Easy development of RESTful API wrapper

## Feature
- Get response as dataclass object you defined
- Return type can be specified by type annotation of api function
- All parameters (query, path variable, or json data) can be specified at once


## install

```
pip install apywrapper
```

## Example

```python
from apywrapper import Apy, delete, get, patch, post, put
from typing import List, no_type_check
from dataclasses import dataclass


@dataclass
class User:
    name: str
    id: str


@no_type_check
class ApiClient(Apy):
    def __init__(self, token, host="https://example.com/api":
        super().__init__(host, headers={"api-token": token})

    @get("/users/")
    def get_users(self) -> List[User]:
        return {}

    @get("/users/{user_id}")
    def get_user(self, user_id) -> User:
        return {"user_id": user_id}

api = ApiClient(token="xxxxxxxxxxxxxxxxxx")
sh1ma = api.get_user("sh1ma") # return User object
```