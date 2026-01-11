from fastapi import FastAPI
from pydantic import BaseModel
from anthropic import Anthropic
import os

# Create FastAPI app
app = FastAPI()

# Read API key from environment variable
client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# Define request body structure
class ChatRequest(BaseModel):
    message: str

# Chat endpoint
@app.post("/chat")
def chat(req: ChatRequest):
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        messages=[
            {"role": "user", "content": req.message}
        ],
        max_tokens=300
    )

    return {
        "reply": response.content[0].text
    }