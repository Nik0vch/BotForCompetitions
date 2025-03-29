from .keyboard import *
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет, я бот для сопровождения олимпиады, чем я могу вам помочь?", reply_markup=KEYBOARD_MAIN)

@router.message(F.text == "Информация об олимпиаде")
async def info(msg: Message):
    await msg.answer("Ну, это олимпиада, чё еще сказать.",)

@router.message(F.text == "Зарегестрироваться")
async def info(msg: Message):
    await msg.answer("Я ещё не привязал бд, жди обновлений.",)
