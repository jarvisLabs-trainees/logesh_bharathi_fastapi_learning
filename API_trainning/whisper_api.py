from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import requests
from typing import List

app = FastAPI()

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large"
Headers = {"Authorization": f"Bearer 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"}

def query_whisper_api(file_content: bytes):
    response = requests.post(API_URL, headers=Headers, data=file_content)
    return response.json()


@app.post("/transcribe")
async def transcribe_file(file: UploadFile):
    try:
        if not file.content_type.startswith("audio/"):
            raise HTTPException(status_code=400, detail="Only audio files are supported.")
        
        file_content = await file.read()
        output = query_whisper_api(file_content)
        return JSONResponse(content=output)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))