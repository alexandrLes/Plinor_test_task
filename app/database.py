from typing import List
from app.models import Event

data_store: List[Event] = []

async def save_event(event: Event):
    data_store.append(event.dict())
