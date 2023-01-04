from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton



kb = InlineKeyboardMarkup(row_width=2)
button1 = InlineKeyboardButton(text="Lol Fun", url="https://developer.mozilla.org/ru/")
button2 = InlineKeyboardButton(text="not intresting", url="https://platform.kata.academy/user/courses")

kb.add(button1).add(button2)

kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button11 = KeyboardButton(text="/links")

kb2.add(button11)


