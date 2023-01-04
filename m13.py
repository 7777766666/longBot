from aiogram import Bot, Dispatcher, executor, types
from config import ID_BOT_LESSON3
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

bot = Bot(ID_BOT_LESSON3)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
b1 = KeyboardButton(text="/help")
b2 = KeyboardButton(text="/mem")
kb.add(b1, b2)


async def lol(_):
    print("Start lol")


@dp.message_handler(commands=["start"])
async def start2(message: types.Message):
    await message.answer(text="Welcome to our Bot", reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=["mem"])
async def mem1(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text="❤️", callback_data="yes")
    ib2 = InlineKeyboardButton(text="👍", callback_data="супер!")
    ikb.add(ib1, ib2)
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://i.ytimg.com/vi/S7pAyHvd0wk/maxresdefault.jpg",
                         caption="Нравятся ли тебе тигры?",
                         reply_markup=ikb)


@dp.callback_query_handler()
async def calltirges(callback: types.CallbackQuery):
    if callback.data == "yes":
        await callback.answer(text="Я знал, что тебе тигры понравятся ❤️")
    await callback.answer("Всем нравятся тигры и ты не исключение  👍️")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=lol, skip_updates=True)
