from fastapi import FastAPI
from pydantic import BaseModel
from TTS.api import TTS
import uuid

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

app = FastAPI()

class TTSRequest(BaseModel):
    text: str

@app.post("/generate-speech")
def generate_speech(req: TTSRequest):
    filename = f"/tmp/{uuid.uuid4()}.wav"
    tts.tts_to_file(text=req.text, file_path=filename)

    with open(filename, "rb") as f:
        audio_bytes = f.read()

    return {"audio_hex": audio_bytes.hex()}
