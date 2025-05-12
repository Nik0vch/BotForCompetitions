from neural.spacyModel import *
from spacy import *
from neural import spacyModel
from aiogram.types import Message
from . import audioService

def GetAttributesWithText(text: str) -> dict[LABELS_NLP, str]:
    return spacyModel.GetAttributes(text)

async def GetAttributesWithVoice(msg: Message):
    text = await audioService.MessageVoiceToText(msg)
    await msg.answer(text  if text != "" else "-")
    return GetAttributesWithText(text)