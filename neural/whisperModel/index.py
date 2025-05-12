import whisper, logging, asyncio, os
from whisper import Whisper

# whisper_model = whisper.load_model("base")
whisper_model: Whisper

def Init():
    global whisper_model
    logging.info("Идёт подключение модели whisper...")
    whisper_model = whisper.load_model("large-v3")

async def WavToText(wav_path: str):
    try:
        result = whisper_model.transcribe(wav_path, language="ru")        
        await asyncio.to_thread(os.remove, wav_path)
        return result["text"]
    except Exception as e:
        logging.error(f"Ошибка при распозновании текста: {e}")