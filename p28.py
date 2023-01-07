from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import KENGURY
from aiogram.utils.callback_data import CallbackData
import asyncio
from aiogram.utils.exceptions import BotBlocked

bot = Bot("5724701366:AAFEQHc0elthrFpat_eSY6PJIK_zIiEdqMA")
dp = Dispatcher(bot=bot)



async def start777(_):
    print("Kenguru")


@dp.message_handler(commands=["s"])
async def st1(mess: types.Message) -> None:
    await asyncio.sleep(10)
    await mess.answer("send message for user")
    return True     #эмитируем блокировку бота


@dp.errors_handler(exception=BotBlocked)
async def error_block(update: types.Update, exception: BotBlocked) -> bool:
    print("Impossible send, we are blocked")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=start777)