from aiogram import Bot, Dispatcher, executor, types



ID_MY_TOKEN = "5724701366:AAFEQHc0elthrFpat_eSY6PJIK_zIiEdqMA"
bot = Bot(ID_MY_TOKEN)

dp = Dispatcher(bot)

async def on_startup(_):
    print("Bot is started")


@dp.message_handler(commands=["start"])
async def any_lol1(message: types.Message):
    await message.answer("<em>Hello</em>, <b>go to</b> our <em>Bot!</em>", parse_mode="html")  #parse_mode="html" we can add html razmtku


@dp.message_handler(commands=["s1"])
async def sticker(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEHGv5js3ciPqPIHJq90U61fqsKFDGbmAACNg8AAh4J8UlSVZzp6JZtey0E")

@dp.message_handler(commands=["s2"])
async def st2(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEHGwABY7N4BZ1KnbTfIzsSyMcPlj_-yCUAAokIAAKLDvhJ_RQj-gABCfmBLQQ")
    message.delete();
@dp.message_handler(commands=["s3"])
async def st2(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEHGwJjs3jtlYoe_ouPZZC-1Skb9zu83AACRxEAAtOk8UlMRnz-PhHACC0E")
    message.delete();

@dp.message_handler()
async def amodzy1(message: types.Message):
    # await message.reply(message.text + " 😅")
    await message.answer(message.text + " 😅" + " LOL!")





if  __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)  #экзекьютер исполняет код/server