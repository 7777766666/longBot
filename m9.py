from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from random import randrange
from config import ID_BOT_LESSON3



bot = Bot(ID_BOT_LESSON3)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("/help")).insert(KeyboardButton("/desc")).add(KeyboardButton("❤️")).insert(KeyboardButton("/send_apple")).add(KeyboardButton("/random"))

async def start1(_):
    print("We are started!!!")

HELP_LOL = """"
/start = go!!!
/help - You are silly
/desc = any lol
/send_apple = apple!!!!
/random - any random place
"""


@dp.message_handler(commands=["start"])
async def lols(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="hello, my friend!!!",
                           reply_markup=keyboard)
    await message.delete()

@dp.message_handler(commands=["desc"])
async def lolsss(message: types.Message):
    await message.answer(text="Desc lol")
    await message.delete()

@dp.message_handler(commands=["help"])
async def tyihk(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP_LOL, reply_markup=keyboard)
    await message.delete()


@dp.message_handler(commands=["send_apple"])
async def send_aple(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id, photo="https://img.freepik.com/premium-photo/red-apple-with-green-leaf-isolated-on-a-white_80510-518.jpg?w=2000")
    await message.delete()

@dp.message_handler(commands=["random"])
async def get_random_place(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            longitude=randrange(1, 100),
                            latitude=randrange(1, 99))
    await message.delete()

@dp.message_handler()
async def send_st2(message: types.Message):
    if message.text.__contains__("❤️"):
        await bot.send_sticker(chat_id=message.from_user.id,
                               sticker="CAACAgIAAxkBAAEHHRZjtHmMxT66wljX-VbvhirLnnPXygAC9SsAAh69QUlwsyA8stdJFi0E")
        # await  (chat_id=message.from_user.id, text="lol ")
        # await bot.send_message(chat_id=message.from_user.id, text="fsticker for you")
        # await message.delete()






if __name__ == "__main__":
    executor.start_polling(dp, on_startup=start1)
