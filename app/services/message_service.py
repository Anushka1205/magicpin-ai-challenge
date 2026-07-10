from app.services.llm_service import generate_ai_response


def generate_reply(history, merchant_context):
    reply = generate_ai_response(history, merchant_context)

    if not reply:
        return "Sorry, Magicpin AI is temporarily unavailable. Please try again in a moment."

    return reply