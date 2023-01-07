from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import KENGURY

bot = Bot(KENGURY)
dp = Dispatcher(bot= bot)

cb = CallbackData("ikb", "action")
ikb = InlineKeyboardMarkup()
# ib1 = InlineKeyboardButton(text="push", callback_data="p")
ib1 = InlineKeyboardButton(text="push", callback_data=cb.new("p"))
ikb.add(ib1)

cb = CallbackData("ikb", "action")

async def start777(_):
    print("KENGURU")


@dp.message_handler(commands=["s"])
async def start1(mes: types.Message):
    await mes.answer(text="test", reply_markup=ikb)
    # await mes.delete()


@dp.callback_query_handler(cb.filter())
async def lolss(call: types.CallbackQuery, callback_data: dict) -> None:
    if callback_data["action"] == "p":
        await call.answer(text="yes, it is working!")


# @dp.callback_query_handler(lambda call: call.data == "p")   # or text =""
# async def cd_hand(callback: types.CallbackQuery) -> None:
#     await callback.answer(text="Some text")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=start777, skip_updates=True)