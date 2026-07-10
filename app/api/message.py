from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.merchant_context_service import get_latest_context
from app.database.database import get_db
from app.schemas.message_schema import (
    MessageRequest,
    MessageResponse,
)

from app.services.conversation_service import (
    get_or_create_conversation,
    save_user_message,
    save_ai_message,
    get_conversation_history,
)

from app.services.message_service import generate_reply

router = APIRouter(
    prefix="/v1",
    tags=["Message"],
)


@router.post(
    "/message",
    response_model=MessageResponse,
)
def message(
    request: MessageRequest,
    db: Session = Depends(get_db),
):

    conversation = get_or_create_conversation(
        db,
        request.conversation_id,
    )

    save_user_message(
        db,
        conversation,
        request.message,
    )

    history = get_conversation_history(
        db,
        conversation,
    )

    merchant_context = get_latest_context(db)

    reply = generate_reply(
        history,
        merchant_context
    )

    save_ai_message(
        db,
        conversation,
        reply,
    )

    return MessageResponse(
        reply=reply
    )