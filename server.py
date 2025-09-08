import os
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = FastAPI()

async def stream_gpt(messages):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
    payload = {
        "model": "gpt-4o-mini",
        "messages": messages,
        "stream": True,
    }
    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream("POST", url, headers=headers, json=payload) as resp:
            async for line in resp.aiter_lines():
                if line.startswith("data: "):
                    data = line[6:].strip()
                    if data == "[DONE]":
                        break
                    yield data.encode("utf-8")

@app.post("/chat")
async def chat(req: Request):
    body = await req.json()
    text = body.get("text", "")
    messages = [
        {"role": "system", "content": "You are an English-Chinese dictionary and language tutor."},
        {"role": "user", "content": f"Please help me explain and learn this word or phrase：{text}"}
    ]
    return StreamingResponse(stream_gpt(messages), media_type="text/event-stream")
