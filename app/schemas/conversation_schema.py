from pydantic import BaseModel
from typing import List


class ConversationMessage(BaseModel):
    sender: str
    content: str


class ConversationResponse(BaseModel):
    conversation_id: str
    messages: List[ConversationMessage]