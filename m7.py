from aiogram import Bot, Dispatcher, executor, types

ID_BOT_T = "5724701366:AAFEQHc0elthrFpat_eSY6PJIK_zIiEdqMA"

bot = Bot(ID_BOT_T)
dp = Dispatcher(bot)

async def start(_):
    print("Bot is working")

HELP2 = """
/start - We are start
/help - I can help
<b>/lol - some fun</b>
/такоесебе = ссылка на русском плохо видна
"""



@dp.message_handler(commands=["help"])
async def help2(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP2, parse_mode="html")
    # await message.delete()

@dp.message_handler(commands=["pic"])
async def pic11(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://aif-s3.aif.ru/images/026/400/1457c444656310b573196d563f431fcb.jpg")
    await message.delete()

@dp.message_handler(commands=["loc"])
async def loc1(message: types.Message):
    await bot.send_location(chat_id = message.from_user.id,
                         latitude = 55.74531666441173,
                         longitude = 37.594509037151944)
    await message.delete()


@dp.message_handler()
async def echo(message: types.Message):
    # await message.answer(message.text )
    await bot.send_message(chat_id=message.chat.id, text="Люблю! В личке стикер! ❤️ ")
    await bot.send_sticker(chat_id=message.from_user.id, sticker="CAACAgIAAxkBAAEHHRZjtHmMxT66wljX-VbvhirLnnPXygAC9SsAAh69QUlwsyA8stdJFi0E")
    await message.delete()



if __name__ == "__main__":
    executor.start_polling(dp, on_startup=start, skip_updates=True)