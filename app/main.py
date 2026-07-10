from fastapi import FastAPI

app = FastAPI(
    title="Magicpin AI Backend Challenge",
    description="AI-powered merchant assistant for Magicpin",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Magicpin AI Backend Challenge is running!"
    }