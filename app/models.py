from pydantic import BaseModel

class Event(BaseModel):
    ts: int
    a: int = None
    b: int = None
    c: int = None
    d: int = None
    e: int = None
    f: int = None
