# Напишите бота, удаляющего из текста все слова, содержащие 'абв'

import time
import logging


from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils import executor

TOKEN = "5658974969:AAGTKm5R2emYZBm1ZyZyRqGMtbPPhDYK5I8"

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = message.text
    filterred = list(filter(lambda x: 'абв' not in x, text.split()))
 
   
    await message.answer(f'{" ".join(filterred)}')



executor.start_polling(dp)