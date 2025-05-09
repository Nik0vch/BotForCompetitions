from .keyboard import *
from sqlalchemy.exc import IntegrityError
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import Message
from services import *
from aiogram import Router
from depend import *
from services import *

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

@router.message()
async def any(msg: Message): 
    # spacyService.train_ner_model()
    # spacyService.train_city()
    attributes = spacyService.GetAttributes(msg.text)
    # print(attributes)
    text = ""
    for key, value in attributes.items():
        text += key + ": " + value + "\n"
    await msg.answer(text)
