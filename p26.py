import random

from aiogram import Bot, Dispatcher, executor, types
from config import KENGURY
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(KENGURY)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=2)
b1 = InlineKeyboardButton(text="Увеличить на 1", callback_data="ikb_plus")
b2 = InlineKeyboardButton(text="уменьшить на 1", callback_data="ikb_minus")
b3 = InlineKeyboardButton(text="Случайное число до 100", callback_data="ikb_random")

ikb.add(b1, b2).add(b3)
n = 0

async def start777(_):
    print("Start Kenruru")


def lols() -> InlineKeyboardMarkup:
    return ikb

@dp.message_handler(commands="s")
async def get_mems(message: types.Message) -> None:
    await message.answer(text=f"число сейчас {n}",
                         reply_markup=lols())
    await message.delete()

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("ikb"))
async def get_ikb(callback: types.CallbackQuery) -> None:
    global n
    if callback.data.__eq__("ikb_plus"):
    # if callback.data == "ikb_plus":
        n +=1
        await callback.message.edit_text(f"число сейчас {n}", reply_markup=lols())
    elif callback.data.__contains__("ikb_minus"):
        n -=1
        await callback.message.edit_text(text=f"число сейчас {n}", reply_markup=lols())
    elif callback.data.__eq__("ikb_random"):
        n = random.randint(0, 100)
        await callback.message.edit_text(text=f"число сейчас {n}", reply_markup=lols())

    else:
        1/0


# @dp.callback_query_handler(lambda callback_query: callback_query.data("random"))
# async def get_random(callback: types.CallbackQuery) ->None:
#     ran = random.randint(0, 1000)
#     await callback.message.answer(text=("ran"))








if __name__ == "__main__":
    executor.start_polling(dp, on_startup=start777, skip_updates=True)


