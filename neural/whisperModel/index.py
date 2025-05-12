import whisper, logging, asyncio, os
from whisper import Whisper
from .interface import WHISPER_MODELS

# whisper_model = whisper.load_model("base")
whisper_model: Whisper

def Init():
    global whisper_model
    modelName = os.environ['WHISPER_MODEL']
    if modelName in WHISPER_MODELS._value2member_map_:
        logging.info("Идёт подключение модели whisper...")
        whisper_model = whisper.load_model(modelName)
    else:
        raise ValueError(f"Неизвестоное наименование Whisper модели: {modelName}")

async def WavToText(wav_path: str):
    try:
        result = whisper_model.transcribe(wav_path, language="ru")        
        await asyncio.to_thread(os.remove, wav_path)
        return result["text"]
    except Exception as e:
        logging.error(f"Ошибка при распозновании текста: {e}")