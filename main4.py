from aiogram import Bot, Dispatcher, types, executor
import string
import random


ID_TOKEN = "5724701366:AAFEQHc0elthrFpat_eSY6PJIK_zIiEdqMA"
count = 0;

bot = Bot(ID_TOKEN);
dp = Dispatcher(bot);

@dp.message_handler(commands=["count"])
async def count1(message: types.Message):
    global count
    await message.answer(f'Вы вызвали /count: {count} раз!')
    await message.delete()
    count +=1;


@dp.message_handler(commands=["lol", "pop", "LOL"])
async def lol1(message: types.Message):
    await message.answer("I can send random letter")
    await message.delete()

@dp.message_handler()
async def random1(message: types.Message):
    await message.reply(random.choice(string.ascii_letters));

if __name__ == "__main__":
    executor.start_polling(dp);

