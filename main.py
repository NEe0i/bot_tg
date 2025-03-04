import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import find_dotenv, load_dotenv
from logura import logger

load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Это была команда старт")


# @dp.message()
# async def echo(message: types.Message):
#    await message.answer(message.text)


@dp.message()
async def convers(message: types.Message):
    if message.text.lower() == "утро":
        await message.answer("Пьем кофе")


async def main():
    await dp.start_polling(bot)

asyncio.run(main())
