## apywrapper

It can make wrapper for RESTful API


## Example

```python
from apywrapper import Api

api = Api("https://httpbin.org/bytes")


@api.get("/{n}")
def get(n: int):
    return {"n": 15}


a = print(get("Hello").text) # print result
```
