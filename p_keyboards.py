from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

kb = ReplyKeyboardMarkup(resize_keyboard=True)  #клавиатура подстраивается под всю ширину без этого метода
bt1 = KeyboardButton(text="/help")
bt2 = KeyboardButton(text="/s")
bt3 = KeyboardButton(text="/sticker")
bt4 = KeyboardButton(text="Random photo")

kb.add(bt1, bt2).add(bt3, bt4)
kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton(text="Random")
bp2 = KeyboardButton(text="main")

kb_photo.add(bp1, bp2)

ikb = InlineKeyboardMarkup(row_width=2)
ikb1 = InlineKeyboardButton(text="❤️", callback_data="like")
ikb2 = InlineKeyboardButton(text="👍", callback_data="super")
ikb3 = InlineKeyboardButton(text="next photo", callback_data="next")
ikb4 = InlineKeyboardButton(text="Main menu", callback_data="main")


ikb.add(ikb1, ikb2).add(ikb3).add(ikb4)
