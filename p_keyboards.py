from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

kb = ReplyKeyboardMarkup(resize_keyboard=True)  #клавиатура подстраивается под всю ширину без этого метода
bt1 = KeyboardButton(text="/help")
bt2 = KeyboardButton(text="/s")
bt3 = KeyboardButton(text="/sticker")
bt4 = KeyboardButton(text="Random photo")

kb.add(bt1, bt2).add(bt3, bt4)
kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton(text="Random")
bp2 = KeyboardButton(text="Main manu")

kb_photo.add(bp1, bp2)
