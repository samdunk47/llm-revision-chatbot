import os
from dotenv import load_dotenv
from fastapi import FastAPI
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
app = FastAPI()

@app.post("/chat")
async def chat(message: str):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": message}]
    )
    return {"response": response.choices[0].message.content}

@app.get("/")
async def root():
    return {"message": "AI Chatbot API running"}