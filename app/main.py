from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from app.chat import handle_message
from app.sessions import create_session, get_session
from app.config import ALLOWED_ORIGINS
from app.database import engine, Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None


@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.post("/chat")
async def chat(req: ChatRequest):
    session_id = req.session_id
    session = get_session(session_id)

    if session is None:
        session_id = create_session()
        session = get_session(session_id)

    reply = handle_message(session, req.message)
    return {
        "reply": reply,
        "session_id": session_id
    }


