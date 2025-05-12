from aiogram.types import Message
from utils.audio_utils import audioParser
from neural import whisperModel

async def MessageVoiceToText(msg: Message) -> str:
    wavPath = await audioParser.MessageVoiceToWav(msg)
    text = await whisperModel.WavToText(wavPath)
    return text
    