from sqlalchemy.orm import Session

from app.database.models import Conversation, Message


def get_or_create_conversation(db: Session, conversation_id: str):
    conversation = (
        db.query(Conversation)
        .filter(Conversation.conversation_id == conversation_id)
        .first()
    )

    if conversation is None:
        conversation = Conversation(
            conversation_id=conversation_id
        )
        db.add(conversation)
        db.commit()
        db.refresh(conversation)

    return conversation


def save_user_message(db: Session, conversation, content: str):
    message = Message(
        conversation_id=conversation.id,
        sender="user",
        content=content
    )

    db.add(message)
    db.commit()


def save_ai_message(db: Session, conversation, content: str):
    message = Message(
        conversation_id=conversation.id,
        sender="assistant",
        content=content
    )

    db.add(message)
    db.commit()


def get_conversation_history(db: Session, conversation):

    messages = (
        db.query(Message)
        .filter(Message.conversation_id == conversation.id)
        .order_by(Message.timestamp.desc())
        .limit(10)
        .all()
    )

    messages.reverse()

    history = []

    for message in messages:
        history.append(
            {
                "role": message.sender,
                "content": message.content
            }
        )

    return history