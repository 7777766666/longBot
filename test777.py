
from aiogram import Bot, Dispatcher, executor, types

bot = Bot("5930354248:AAGtL1XeJTu0P84wz-FMHZAWRKiFhajlHwk")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ Эхо-бот от Lol!\nТупо тролю.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)