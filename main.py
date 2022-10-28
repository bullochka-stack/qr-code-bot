import os

import qrcode
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = ''

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.answer(f'Я бот-генератор QR-кодов. Приятно познакомиться, {msg.from_user.first_name}. Отправь мне ссылку или текст и я тебе пришлю код.')


@dp.message_handler()
async def send_code(msg: types.Message):
    data = msg.text
    img = qrcode.make(data)
    img.save(f'media/{msg.from_user.id}-{msg.date.date()}.png')
    img = open(f'media/{msg.from_user.id}-{msg.date.date()}.png', 'rb')
    await msg.answer_photo(img, caption=f'Ваш QR-код: {msg.text}')

    os.remove(f'media/{msg.from_user.id}-{msg.date.date()}.png')


if __name__ == '__main__':
   executor.start_polling(dp)