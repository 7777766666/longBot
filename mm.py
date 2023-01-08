from aiogram import Bot, Dispatcher, executor, types
from config import PP777Bot
from p_keyboards import kb, kb_photo, ikb
from aiogram.dispatcher.filters import Text
import random
from aiogram.types import ReplyKeyboardRemove

bot = Bot(token=PP777Bot) # создаем экземпляр класса Бот
dp = Dispatcher(bot=bot)  #передаем в диспетчер экземпляр бота

HELP_COMMAND = """"
<b>/help - так и быть, помогу</b>
<em>/s - начало положено!</em>
<b>/sticker - пришлю стике</b>
/Random - test!!!!
"""

arr_photos = [
    "https://fotorelax.ru/wp-content/uploads/2016/02/Beautiful-photos-and-pictures-on-different-topics-01.jpg",
    "https://fotorelax.ru/wp-content/uploads/2016/02/Beautiful-photos-and-pictures-on-different-topics-03.jpg",
    "https://fotorelax.ru/wp-content/uploads/2016/02/Beautiful-photos-and-pictures-on-different-topics-09.jpg",
    "https://klike.net/uploads/posts/2019-11/1572611113_3.jpg",
    "https://klike.net/uploads/posts/2019-11/1572611141_4.jpg",
    "https://klike.net/uploads/posts/2019-11/1572611084_5.jpg",
    "https://klike.net/uploads/posts/2019-11/1572611157_16.jpg",
    "https://klike.net/uploads/posts/2019-11/1572611118_23.jpg",
    "https://klike.net/uploads/posts/2019-11/1572611191_29.jpg",
    "https://klike.net/uploads/posts/2019-11/1572611201_39.jpg",
    "https://klike.net/uploads/posts/2019-11/1572611139_40.jpg",
    "https://klike.net/uploads/posts/2019-11/1572611125_42.jpg",
    "https://klike.net/uploads/posts/2022-08/1661329264_307.jpg"

]

photos = dict(zip(arr_photos, ["Bear", "Tiger", "Белка", "смешно1", "смешно2", "смешно3", "смешно4", "смешно5", "смешно6", "смешно7", "смешно8", "смешно9", "смешно10"]))
random_photo = random.choice(list(photos.keys()))

flag = False

async def start777(_):  #запускается экзекьютером при запуске, чтоб было видно, что блот стартовал
    print("start777")

async def send_random10(message: types.Message):
    global random_photo
    random_photo = random.choice(list(photos.keys()))
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random_photo,
                         caption=photos[random_photo],
                         reply_markup=ikb)



@dp.message_handler(Text(equals="Random photo"))
async def open_kb_photo(message: types.Message):
    await message.answer(text="Random photo",
                         reply_markup=ReplyKeyboardRemove())
    await send_random10(message)
    await message.delete()





@dp.message_handler(Text(equals="Main menu"))
async def get_main_manu(message: types.Message):
    await message.answer(text="Return to main",
                         reply_markup=kb)
    await message.delete()

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



@dp.message_handler(commands=["lol"])
async def test1(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="В личку должен написать сообщение")



@dp.callback_query_handler()
async def call_back_random_photo(callback: types.CallbackQuery):
    global random_photo
    global flag
    if callback.data == "like":
        if not flag:
            await callback.answer("Это просто офигенно!")
            flag = not flag
        else:
            await callback.answer("Вы уже лайкали. Больше нельзя!")
        # await callback.message.answer("Это просто офигенно!")
    elif callback.data == "super":
        # await callback.message.answer("Просто отпад!")
        await callback.answer("Отпад!")
    elif callback.data == "main":
        await callback.message.answer(text="Добро пожаловать в главное меню!",
                                      reply_markup=kb)
        await callback.message.delete()
        await callback.answer()
    else:
        random_photo = random.choice(list(filter(lambda x: x != random_photo, list(photos.keys()))))
        await callback.message.edit_media(types.InputMedia(media=random_photo,
                                                           type="photo",
                                                           caption=photos[random_photo]),
                                          reply_markup=ikb)
        await callback.answer()


@dp.message_handler(commands=["loc"])
async def loc_rand(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            longitude=random.randrange(1, 100),
                            latitude=random.randrange(1, 98))


if __name__ == "__main__":   #запускаем непомредственно (не аппосредовано) тут
    executor.start_polling(dispatcher=dp, on_startup=start777, skip_updates=True) # выполнет