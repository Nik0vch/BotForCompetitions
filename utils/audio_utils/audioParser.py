from aiogram.types import Message, Voice
import os
import ffmpeg
import logging
import asyncio

async def MessageVoiceToWav(msg: Message) -> str:
    """
    Возвращает путь к файлу .wav
    """
    voice: Voice = msg.voice
    
    # Получаем информацию о файле
    file = await msg.bot.get_file(voice.file_id)

    # Формируем пути
    ogg_path = os.path.join("utils/audio_utils/voices", f"{voice.file_unique_id}.ogg")
    wav_path = os.path.join("utils/audio_utils/voices", f"{voice.file_unique_id}.wav")

    # Скачиваем файл
    await msg.bot.download_file(file.file_path, ogg_path)

    if not os.path.exists(ogg_path):
        return

    # Конвертируем OGG в WAV через ffmpeg-python
    try:
        (
            ffmpeg
            .input(ogg_path)
            .output(wav_path, format="wav")
            .run(cmd=["ffmpeg", "-v", "quiet"], overwrite_output=True)
        )
    except Exception as e:
        logging.error("Ошибка при конвертации:", str(e))
        return
    
    await asyncio.to_thread(os.remove, ogg_path)
    return wav_path