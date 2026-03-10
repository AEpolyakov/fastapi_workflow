from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class EventType(str, Enum):
    click='click'
    on_hover='on_hover'


class Event(BaseModel):
    event_time: datetime
    user_id: int
    event_type: EventType
