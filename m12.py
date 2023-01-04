from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from config import ID_BOT_LESSON3
from keyboards import kb2, kb  #button1, button2, button11

bot = Bot(ID_BOT_LESSON3)
dp = Dispatcher(bot)


async def start333(_):
    print("@@@@@@@")

@dp.message_handler(commands=["start"])
async def dsff(message: types.Message):
    await message.answer("Main", reply_markup=kb2)



@dp.message_handler(commands=["links"])
async def link_ttt(message: types.Message):
    await message.answer(text="Choose option", reply_markup=kb)






if __name__ == "__main__":
    executor.start_polling(dp, on_startup=start333, skip_updates=True)