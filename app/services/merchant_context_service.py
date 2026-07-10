import json

from sqlalchemy.orm import Session

from app.database.models import MerchantContext


def get_latest_context(db: Session):
    """
    Returns the latest merchant context.
    """

    context = (
        db.query(MerchantContext)
        .order_by(MerchantContext.version.desc())
        .first()
    )

    if context is None:
        return None

    return {
        "context_id": context.context_id,
        "scope": context.scope,
        "version": context.version,
        "payload": json.loads(context.payload)
    }