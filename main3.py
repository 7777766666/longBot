from aiogram import Bot, Dispatcher, types, executor


TOKEN_API ="5724701366:AAFEQHc0elthrFpat_eSY6PJIK_zIiEdqMA"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler()
async def ttttttttttttt(message: types.Message):
    await message.answer(text=message.text.upper())

if __name__ == "__main__":
    executor.start_polling(dp);


