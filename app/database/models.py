from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.database import Base


class MerchantContext(Base):
    __tablename__ = "merchant_contexts"

    id = Column(Integer, primary_key=True, index=True)
    context_id = Column(String, unique=True, nullable=False)
    scope = Column(String)
    version = Column(Integer)
    payload = Column(Text)

    conversations = relationship("Conversation", back_populates="merchant")


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(String, unique=True, nullable=False)

    merchant_id = Column(
        Integer,
        ForeignKey("merchant_contexts.id")
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    merchant = relationship(
        "MerchantContext",
        back_populates="conversations"
    )

    messages = relationship(
        "Message",
        back_populates="conversation"
    )


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)

    conversation_id = Column(
        Integer,
        ForeignKey("conversations.id")
    )

    sender = Column(String, nullable=False)

    content = Column(Text, nullable=False)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )

    conversation = relationship(
        "Conversation",
        back_populates="messages"
    )