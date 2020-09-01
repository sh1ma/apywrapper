from apywrapper import Apy, get
from dataclasses import dataclass


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


class Chatwork(Apy):
    def __init__(self, token):
        super().__init__(
            host="https://api.chatwork.com/v2", headers={"X-ChatWorkToken": token}
        )

    @get("/rooms/{room_id}")
    def get_room(self, room_id: int):
        return (
            Room,
            {"room_id": room_id},
        )  # Return Object, Request Params(Path Args, Query or JsonData(Dict))

    @get("/rooms")
    def get_rooms(self):
        return Room, {}


api = Chatwork(token="xxxxx")
print(api.get_rooms())
