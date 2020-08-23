## apywrapper

It can make wrapper for RESTful API


## Example

```python
import typing
from src.apywrapper import Api
from dataclasses import dataclass

app_id = "X" change this
headers = {"app-id": app_id}

api = Api("https://dummyapi.io/data/api/", headers=headers)


@dataclass
class User:
    id: str
    title: str
    firstName: str
    lastName: str
    gender: str
    email: str
    dateOfBirth: str
    registerDate: str
    phone: str
    picture: str
    location: typing.Dict


@api.get("/user/{user_id}")
def get_user(user_id):
    return User, {"user_id": user_id}


print(get_user("0F8JIqi4zwvb77FGz6Wt")) # dummy user id
```
