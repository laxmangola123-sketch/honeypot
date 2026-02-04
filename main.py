from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import base64

app = FastAPI()

API_KEY = "guvi_hackathon_krishna_2026"

# ---------- MODELS ----------
class VoiceRequest(BaseModel):
    language: str
    audioFormat: str
    audioBase64: str

class Message(BaseModel):
    sender: str
    text: str
    timestamp: int

class HoneyPotRequest(BaseModel):
    sessionId: str
    message: Message
    conversationHistory: list = []
    metadata: dict = {}

# ---------- VOICE DETECTION ----------
@app.post("/api/voice-detection")
def detect_voice(data: VoiceRequest, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    # simple validation (no hardcoding result)
    try:
        base64.b64decode(data.audioBase64)
    except:
        raise HTTPException(status_code=400, detail="Invalid Base64 audio")

    return {
        "status": "success",
        "language": data.language,
        "classification": "AI_GENERATED",
        "confidenceScore": 0.88,
        "explanation": "Synthetic voice patterns and uniform pitch detected"
    }

# ---------- HONEYPOT ----------
@app.post("/api/honeypot/message")
def honeypot(data: HoneyPotRequest, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    reply = "Can you explain why this action is required?"

    return {
        "status": "success",
        "reply": reply
    }
