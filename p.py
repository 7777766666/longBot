from aiogram import Bot, Dispatcher, executor, types
from config import PP777Bot
from p_keyboards import kb


bot = Bot(token=PP777Bot) # создаем экземпляр класса Бот
dp = Dispatcher(bot=bot)  #передаем в диспетчер экземпляр бота

HELP_COMMAND = """"
<b>/help - так и быть, помогу</b>
<em>/s - начало положено!</em>
<b>/sticker - пришлю стике</b>
"""

async def start777(_):  #запускается экзекьютером при запуске, чтоб было видно, что блот стартовал
    print("start777")

@dp.message_handler(commands=["s"])
async def command_start(message: types.Message):
    await message.answer(text="Добро пожаловать в наш бот 👍", #тут ответ всегда в личку при мессейдж ансвер
                         reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=["help"])
async def command_help(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,  text=HELP_COMMAND, parse_mode="html")

@dp.message_handler(commands=["sticker"])
async def command_desc(message: types.Message):
    await message.answer(text="I super Bot and I can send random sticker")
    await bot.send_sticker(chat_id=message.chat.id, sticker="CAACAgIAAxkBAAEHIJNjtiALX3BGX9cKleaFaa9CHHx7KAACUQADwDZPExTRqeEWVGi2LQQ")
    await message.delete()




if __name__ == "__main__":   #запускаем непомредственно (не аппосредовано) тут
    executor.start_polling(dispatcher=dp, on_startup=start777, skip_updates=True) # выполнет