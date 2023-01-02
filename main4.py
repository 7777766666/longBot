from aiogram import Bot, Dispatcher, types, executor
import string
import random


ID_TOKEN = "5724701366:AAFEQHc0elthrFpat_eSY6PJIK_zIiEdqMA"

bot = Bot(ID_TOKEN);
dp = Dispatcher(bot);


@dp.message_handler(commands=["lol", "pop", "LOL"])
async def lol1(message: types.Message):
    await message.answer("I can send random letter")
    await message.delete()

@dp.message_handler()
async def random1(message: types.Message):
    await message.reply(random.choice(string.ascii_letters));

if __name__ == "__main__":
    executor.start_polling(dp);

