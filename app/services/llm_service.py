import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = "models/gemini-2.0-flash-001"
print(f"Using Gemini model: {MODEL}")


def generate_ai_response(history, merchant_context=None):

    system_prompt = """
You are Magicpin's AI Merchant Assistant.

Your responsibilities:
- Help merchants increase sales.
- Suggest marketing ideas.
- Recommend promotions.
- Help improve ratings and reviews.
- Give concise and actionable responses.
- Be friendly and professional.
"""

    if merchant_context:
        payload = merchant_context["payload"]

        system_prompt += f"""

Merchant Details:
- Name: {payload.get("name", "")}
- Category: {payload.get("category", "")}
- City: {payload.get("city", "")}
"""

    conversation = ""

    for message in history:
        conversation += f"{message['role']}: {message['content']}\n"

    final_prompt = f"""
{system_prompt}

Conversation:
{conversation}

Assistant:
"""

    try:
        start = time.time()

        response = client.models.generate_content(
            model=MODEL,
            contents=final_prompt,
            config=types.GenerateContentConfig(
                temperature=0.3,
                max_output_tokens=60,
            ),
        )

        print(f"Gemini Response Time: {time.time() - start:.2f} seconds")
        print("Prompt length:", len(final_prompt))
        print("Gemini Response:", response)

        # Always return a valid string
        if hasattr(response, "text") and response.text:
            return response.text

        return "Sorry, I couldn't generate a response at the moment."

        return response.text

    except Exception as e:
        print("Gemini Error:", e)
        return "Sorry, Magicpin AI is temporarily unavailable. Please try again later."