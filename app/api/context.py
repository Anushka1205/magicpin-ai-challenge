from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.context_schema import (
    ContextRequest,
    ContextResponse,
)
from app.services.context_service import save_context

router = APIRouter(
    prefix="/v1",
    tags=["Context"],
)


@router.post(
    "/context",
    response_model=ContextResponse,
)
def create_context(
    request: ContextRequest,
    db: Session = Depends(get_db),
):

    save_context(db, request)

    return ContextResponse(
        accepted=True
    )