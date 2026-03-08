from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
from api.routers import diary

load_dotenv()

app = FastAPI(
    title="Sunflower Destiny Diary",
    description="A personal diary backend combining Notion and Chinese Astrology (Bazi/Ganzhi).",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome to Sunflower Destiny Diary! The stars are aligned."}

app.include_router(diary.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
