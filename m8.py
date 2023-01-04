# from config import ID_BOT_LESSON3
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# ReplyKeyboardMarkup создает объект клавиатуры для удобного взаимодействия с ботом
# KeyboardButton кнопка
# ReplyKeyboardRemove удаление из интерфейса пользователя клавиатуры

from aiogram import Bot, Dispatcher, executor, types


ID_BOT_TOO = "5724701366:AAFEQHc0elthrFpat_eSY6PJIK_zIiEdqMA"
bot = Bot(ID_BOT_TOO)
dp = Dispatcher(bot)



keyboard = ReplyKeyboardMarkup(resize_keyboard=True)       #size keyboard
button1 = KeyboardButton("/help")
# button2 = KeyboardButton("/start")
button3 = KeyboardButton("/love")
button4 = KeyboardButton("/photo")

keyboard.add(button1).insert(button3).add(button4)

HELP_ANY = """
/help - помогите кто может
/start = мы можем начать
<b>/love = Super</b> 
<b>/photo - funny</b> 
"""


async def start_lol(_):
    print("Vah Vax Vax")


@dp.message_handler(commands=["help"])
async def mem1(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=HELP_ANY,
                           parse_mode="html")  #убираем клавиатуру
    # await message.delete()


@dp.message_handler(commands=["start"])
async def start1(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Hello, my young friend", reply_markup=keyboard)
    await message.delete()


@dp.message_handler(commands=["love"])
async def mem1(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Люблю ❤️ ", reply_markup=keyboard)
    await message.delete()


@dp.message_handler(commands=["photo"])
async def chisto_porjat(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         reply_markup=keyboard,photo="https://i.ytimg.com/vi/UKUm1yTFRR0/maxresdefault.jpg")
    await message.delete()


# if __name__ == "__main__":
#     executor.start_polling(dp, on_startup=start_lol, skip_updates=True)

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=start_lol)
