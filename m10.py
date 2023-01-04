from aiogram import Bot, Dispatcher, executor, types
from config import ID_BOT_LESSON3
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup



bot = Bot(ID_BOT_LESSON3)
dp = Dispatcher(bot)

inline_keyboard = InlineKeyboardMarkup(row_width=2)
inline_keyboard_button1 = InlineKeyboardButton(text = "first", url = "https://wikium.ru/train")
inline_keyboard_button2 = InlineKeyboardButton(text="second", url = "https://kata.academy/")

inline_keyboard.add(inline_keyboard_button1, inline_keyboard_button2)

async def start66(_):
    print("!!!!!!!!!")


@dp.message_handler(commands=["start"])
async def lolol(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Wow, hello my friend" ,
                           reply_markup=inline_keyboard)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=start66)