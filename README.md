# Magicpin AI Merchant Assistant

An AI-powered merchant assistant built using FastAPI, SQLite, SQLAlchemy, and Google's Gemini API. The application helps merchants receive AI-powered business suggestions while maintaining conversation history and merchant context.

---

## Features

- Merchant Context Management
- AI Chat Assistant
- Conversation History
- FastAPI REST APIs
- SQLite Database
- SQLAlchemy ORM
- Gemini AI Integration
- React Frontend
- Error Handling & Fallback Responses

---

## Tech Stack

### Backend
- Python 3.13
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Google Gemini API

### Frontend
- React
- Vite
- Axios

---

## Project Structure

magicpin-ai-challenge/

├── app/

│ ├── api/

│ ├── database/

│ ├── schemas/

│ ├── services/

│ └── main.py

├── frontend/

├── .env

├── requirements.txt

└── README.md

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd magicpin-ai-challenge
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_API_KEY
MODEL_NAME=gemini-3.5-flash
DATABASE_URL=sqlite:///./magicpin.db
```

---

## Running the Backend

```bash
uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

## API Endpoints

### Health Check

```
GET /health
```

### Save Merchant Context

```
POST /v1/context
```

### Chat with AI

```
POST /v1/message
```

---

## Database

The application uses SQLite with SQLAlchemy ORM.

Tables:

- MerchantContext
- Conversation
- Message

---

## AI Workflow

1. Merchant context is stored.
2. User sends a message.
3. Conversation history is fetched.
4. Merchant context is added to the prompt.
5. Gemini API generates a response.
6. AI response is stored in the database.
7. Response is returned to the frontend.

---

## Error Handling

The application gracefully handles:

- Invalid requests
- Database errors
- Gemini API failures
- Temporary AI service unavailability

When the Gemini API is temporarily unavailable, the application returns a fallback response instead of crashing.

---

## Notes

The application integrates with Google's Gemini API. During testing, the external AI service may occasionally return temporary availability errors (for example, HTTP 503 due to high demand). The application handles these situations gracefully and continues to return a valid response to the client.

---
