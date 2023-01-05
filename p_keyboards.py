from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

kb = ReplyKeyboardMarkup(resize_keyboard=True)  #клавиатура подстраивается под всю ширину без этого метода
bt1 = KeyboardButton(text="/help")
bt2 = KeyboardButton(text="/s")
bt3 = KeyboardButton(text="/sticker")

kb.add(bt1, bt2).add(bt3)