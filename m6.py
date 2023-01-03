# from aiogram import Bot, Dispatcher, executor, types
from aiogram import Bot, Dispatcher, executor, types

ID_MY = "5724701366:AAFEQHc0elthrFpat_eSY6PJIK_zIiEdqMA"
bot = Bot(ID_MY)

dp = Dispatcher(bot)
async def lol_on_startup(_):
    print("Bot is start!!!")


@dp.message_handler(commands=["give"])
async def giv333(message: types.Message):
    await message.answer("<b>Смотри</b>, <em>какой смешной кот</em>" + '❤️', parse_mode="html")
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEHGxhjs46hE0TzSmzRwbqZsZdvQaBWvwACxgoAAhf-gUojb09iakYCMC0E")


@dp.message_handler()
async def health(message: types.Message):
    if '❤️' in message.text:
        await message.answer('🖤')

if __name__ == "__main__":
    # executor.start_polling(dp)
    executor.start_polling(dp, on_startup=lol_on_startup)


