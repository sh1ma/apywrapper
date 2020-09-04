## apywrapper

![lint](https://github.com/sh1ma/apywrapper/workflows/lint/badge.svg?branch=develop)

Easy development of RESTful API wrapper


## install

```
pip install apywrapper
```


## Example (Chatwork API Wrapper)

```python
from apywrapper import Apy
from dataclasses import dataclass

api = Apy(
    "https://api.chatwork.com/v2",
    headers={"X-ChatWorkToken": "xxxxxxxxx"},
)


@dataclass
class Room:
    room_id: int
    name: str
    type: str
    role: str
    sticky: bool
    unread_num: int
    mention_num: int
    mytask_num: int
    message_num: int
    file_num: int
    task_num: int
    icon_path: str
    last_update_time: int


@api.get("/rooms/{room_id}")
def get_room(room_id: int):
    return (
        Room,
        {"room_id": room_id},
    )  # Return Object, Request Params(Path Args, Query or JsonData(Dict))


@api.get("/rooms")
def get_rooms():
    return Room, {}


print(get_room(113377551))  # return Room
print(get_rooms()) # return List[Room]

```

## Example (POST data)
```python
@api.post("/users")
def create_user(username: str, user_id: str):
    return User, {"user_name": username, "user_id": user_id}

created_user = create_user("sh1ma", "sh1ma")
```

## Example (GET with `is_hello` query)
```python
@api.get("/users/{user_id}")
def get_user(user_id: str, is_hello: bool):
    return User, {"user_id": user_id, "is_hello": True}
```

