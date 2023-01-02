from aiogram import Bot, Dispatcher, types, executor

HELP_COMMAND = """
/help - all commands

/start - we are start 
"""


TOKEN_API ="5724701366:AAFEQHc0elthrFpat_eSY6PJIK_zIiEdqMA" #токен

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=["help"])
async def help1(message: types.Message):
    await message.reply(text=HELP_COMMAND)


@dp.message_handler(commands=["start"])
async def help2(message: types.Message):
    await message.answer(text="You are welcom to our Bot")
    await message.delete();


if __name__ == "__main__":
    executor.start_polling(dp)