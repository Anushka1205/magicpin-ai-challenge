from pydantic import BaseModel
from typing import Dict, Any


class ContextRequest(BaseModel):
    scope: str
    context_id: str
    version: int
    payload: Dict[str, Any]


class ContextResponse(BaseModel):
    accepted: bool