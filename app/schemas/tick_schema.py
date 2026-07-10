from pydantic import BaseModel
from typing import List


class TickRequest(BaseModel):
    now: str
    available_triggers: List[str]


class Action(BaseModel):
    merchant_id: str
    body: str
    cta: str


class TickResponse(BaseModel):
    actions: List[Action]