import json

from sqlalchemy.orm import Session

from app.database.models import MerchantContext


def save_context(db: Session, context):

    existing = (
        db.query(MerchantContext)
        .filter(MerchantContext.context_id == context.context_id)
        .first()
    )

    if existing:
        existing.scope = context.scope
        existing.version = context.version
        existing.payload = json.dumps(context.payload)

    else:
        existing = MerchantContext(
            context_id=context.context_id,
            scope=context.scope,
            version=context.version,
            payload=json.dumps(context.payload),
        )

        db.add(existing)

    db.commit()

    return True