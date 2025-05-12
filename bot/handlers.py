from .keyboard import *
from sqlalchemy.exc import IntegrityError
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from services import *
from aiogram import Router
from depend import *
from services import *
import logging

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет, я бот для сопровождения олимпиады, чем я могу вам помочь?", reply_markup=KEYBOARD_MAIN)

@router.message(F.text == "Информация об олимпиаде")
async def info(msg: Message):
    await msg.answer("Ну, это олимпиада, чё еще сказать.",)

@router.message(F.text == "Зарегестрироваться")
async def regist(msg: Message):
    try:
        async for db in GetDbSession():
            await participantService.CreateUser(db, msg.from_user.full_name, msg.from_user.id)
            await msg.answer("Вы успешно зарегестрированы.",)
    except IntegrityError as e:
        await msg.answer("Вы уже зарегестрированы.",)

@router.message(F.voice)
async def handle_voice(msg: Message):
    try:
        text = ""
        attributes = await spacyService.GetAttributesWithVoice(msg)
        for key, value in attributes.items():
            text += key + ": " + value + "\n"
        await msg.answer(f"{text}"  if text != "" else "-")
    except Exception as e:
        await msg.answer("⚠️ Произошла ошибка при обработке голосового сообщения.")
        logging.error(e)
