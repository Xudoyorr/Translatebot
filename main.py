from buttons import menu,orqa
from aiogram.dispatcher.filters import Text

import logging

from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def boshlash(message: types.Message):
    """Botga /start buyrug'i yozilganda ishga tushadi"""
    user = message.from_user.first_name
    await message.reply(f"Salom 😊{user}",reply_markup=menu)
    await message.reply("Matnlarni tarjima qilish uchun tugmalardan birini tanlang✅")

@dp.message_handler()
async def echo(message: types.Message):
    id = message.chat.id
@dp.message_handler(Text(equals="Tarjima qilmoqchi bolgan matnni kiriting😊"))
async def echo(message: types.Message):
    await message.answer('matn kiriting',reply_markup=orqa)

@dp.message_handler(Text(equals='Orqaga🔙'))
async def sshfj(message):
    await menu.answer('Menu',reply_markup=menu)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)  