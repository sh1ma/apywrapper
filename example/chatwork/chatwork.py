from apywrapper import Apy
from dataclasses import dataclass

api = Apy("https://api.chatwork.com/v2", headers={"X-ChatWorkToken": "xxxx"})


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


print(get_room(183377745))  # return Room Object

