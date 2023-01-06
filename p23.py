from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from config import PP777Bot

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="❤️", callback_data="like"),
     InlineKeyboardButton(text="😡", callback_data="disLike")],
])

bot = Bot(token=PP777Bot)
dp = Dispatcher(bot=bot)

async def start777(_):
    print("Lol start")


@dp.message_handler(commands=["start"])
async def lol22(message: types.Message) ->None:
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://static.mk.ru/upload/entities/2021/12/30/13/articles/facebookPicture/98/6c/35/53/8f2366d82d085e1935353c2ec0706f1c.jpg",
                         caption="нравиться ли тебе фотография?",
                         reply_markup=ikb)
    await message.delete()

@dp.callback_query_handler()
async def ikb11(callback: types.CallbackQuery):
    print(callback)
    if callback.data == "like":
        await callback.answer("Foto is the best!")
    await callback.answer("Не заслуженный дизлайк(((")

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=start777)

