from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ikb = InlineKeyboardMarkup(row_width=2)

b1 = InlineKeyboardButton("❤️ Bау, очень круто!", callback_data="like")
b2 = InlineKeyboardButton("🙈 Такая себе фоточка(((", callback_data="dis" )
b3 = InlineKeyboardButton("close keyboard", callback_data="close")

ikb.add(b1, b2).add(b3)
# ikb.add(b1, b2)