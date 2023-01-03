# from aiogram import Bot, Dispatcher, executor, types
from aiogram import Bot, Dispatcher, executor, types
import string


ID_MY = "5724701366:AAFEQHc0elthrFpat_eSY6PJIK_zIiEdqMA"
bot = Bot(ID_MY)

dp = Dispatcher(bot)

HELP_COMMAND = """

<b>/help  </b> - lol
/start - hello
<em>/mem</em>     - просто мем
"""


async def lol_on_startup(_):
    print("Bot is start!!!")


@dp.message_handler(commands=["help"])
async def help66(message: types.Message):
    await message.reply(HELP_COMMAND, parse_mode="html")

@dp.message_handler(content_types=["sticker"])
async def st10(message: types.Message):
    await message.answer(message.sticker.file_id)



@dp.message_handler()
async def count22(message: types.Message):
    await message.answer(text=str(message.text.count("✅")))

@dp.message_handler(commands=["give"])
async def give333(message: types.Message):
    await message.answer("<b>Смотри</b>, <em>какой смешной кот</em>" + '❤️', parse_mode="html")
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEHGxhjs46hE0TzSmzRwbqZsZdvQaBWvwACxgoAAhf-gUojb09iakYCMC0E")


@dp.message_handler()
async def health(message: types.Message):
    if '❤️' in message.text:
        await message.answer('🖤')






if __name__ == "__main__":
    # executor.start_polling(dp)
    executor.start_polling(dp, on_startup=lol_on_startup)


