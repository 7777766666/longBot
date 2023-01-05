from aiogram import Bot, Dispatcher, executor, types
from config import PP777Bot
from p_keyboards import kb, kb_photo
from aiogram.dispatcher.filters import Text
import random

bot = Bot(token=PP777Bot) # создаем экземпляр класса Бот
dp = Dispatcher(bot=bot)  #передаем в диспетчер экземпляр бота

HELP_COMMAND = """"
<b>/help - так и быть, помогу</b>
<em>/s - начало положено!</em>
<b>/sticker - пришлю стике</b>
/Random - test!!!!
"""

async def start777(_):  #запускается экзекьютером при запуске, чтоб было видно, что блот стартовал
    print("start777")

arr_photos = [
    "https://fotorelax.ru/wp-content/uploads/2016/02/Beautiful-photos-and-pictures-on-different-topics-01.jpg",
    "https://fotorelax.ru/wp-content/uploads/2016/02/Beautiful-photos-and-pictures-on-different-topics-03.jpg",
    "https://fotorelax.ru/wp-content/uploads/2016/02/Beautiful-photos-and-pictures-on-different-topics-09.jpg"

]



@dp.message_handler(Text(equals="Random photo"))
async def open_kb_photo(message: types.Message):
    await message.answer(text="Random photo enter Random",
                         reply_markup=kb_photo)
    await message.delete()

@dp.message_handler(Text(equals="Random"))
async def get_randon1(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random.choice(arr_photos))
    await message.delete()


@dp.message_handler(Text(equals="Main manu"))
async def get_main_manu(message: types.Message):
    await message.answer(text="Return to main",
                         reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=["s"])
async def command_start(message: types.Message):
    await message.answer(text="Добро пожаловать в наш бот 👍", #тут ответ всегда в личку при мессейдж ансвер
                         reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=["help"])
async def command_help(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,  text=HELP_COMMAND, parse_mode="html")

@dp.message_handler(commands=["sticker"])
async def command_desc(message: types.Message):
    await message.answer(text="I super Bot and I can send random sticker")
    await bot.send_sticker(chat_id=message.chat.id, sticker="CAACAgIAAxkBAAEHIJNjtiALX3BGX9cKleaFaa9CHHx7KAACUQADwDZPExTRqeEWVGi2LQQ")
    await message.delete()


@dp.message_handler(commands=["lol"])
async def test1(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="В личку должен написать сообщение")




if __name__ == "__main__":   #запускаем непомредственно (не аппосредовано) тут
    executor.start_polling(dispatcher=dp, on_startup=start777, skip_updates=True) # выполнет