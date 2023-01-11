from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

storage = MemoryStorage()
KENGURY = "5930354248:AAGtL1XeJTu0P84wz-FMHZAWRKiFhajlHwk"
proxy_url = 'http://proxy.server:3128'
bot = Bot(KENGURY, proxy=proxy_url)
dp = Dispatcher(bot, storage=storage)

# proxy_url = 'http://proxy.server:3128'
# bot = Bot(token="5930354248:AAGtL1XeJTu0P84wz-FMHZAWRKiFhajlHwk", proxy=proxy_url)


class ProfileStatesGroup(StatesGroup):
    photo = State()
    name = State()
    age = State()
    description = State()

def get_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("/create"))
    return kb


def get_cancel_kb() -> ReplyKeyboardMarkup:
    kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
    kb2.add(KeyboardButton("/cancel"))
    return kb2


async def start777(_):
    print("KENGURY")


@dp.message_handler(commands=["cancel"], state="*")
async def cmd_cancel1(mess: types.Message, state: FSMContext):
    if state is None:
        return

    await state.finish()
    await mess.reply(text="Вы прервали заполнение профиля!",
                     reply_markup=get_kb())


@dp.message_handler(commands=["start"])
async def cmd_start(mess: types.Message) -> None:
    await mess.answer(text="Желаете заполнить Ваш профиль /create",
                      reply_markup=get_kb())


@dp.message_handler(commands=["create"])
async def cmd_create(mess: types.Message) -> None:
    await mess.reply(text="Давайте оформим Ваш профиль. Пришлит своё фото.",
                     reply_markup=get_cancel_kb())
    await ProfileStatesGroup.photo.set()    #устанавливаем состояние на ожидание фото


@dp.message_handler(lambda message: not message.photo, state=ProfileStatesGroup.photo)
async def check_photo(mess: types.Message):
    await mess.reply("Это не фотография!")


@dp.message_handler(content_types=["photo"], state=ProfileStatesGroup.photo)
async def load_photo(mess: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["photo"] = mess.photo[0].file_id

    await mess.reply(text="Введите Ваше имя")
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.name)
async def load_name(mess: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["name"] = mess.text

    await mess.answer(text="Сколько Вам лет?")
    await ProfileStatesGroup.next()


@dp.message_handler(lambda mess: not mess.text.isdigit() or float(mess.text) > 90, state=ProfileStatesGroup.age)
async def check_age(mess: types.Message):
    await mess.answer(text="Введите Ваш реальный возраст (число)")


@dp.message_handler(state=ProfileStatesGroup.age)
async def load_age(mess: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["age"] = mess.text

    await mess.answer(text="Задача, которую Вы хотите решить")
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.description)
async def load_description(mess: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["description"] = mess.text
        await bot.send_photo(chat_id=mess.chat.id,
                             photo=data["photo"],
                             caption=f"Ваше имя: {data['name']}\nВам: {data['age']} лет\nЗадача: {data['description']} ")

    await mess.reply(text="Спасибо, Ваш профиль полностью заполнен!")
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=start777, skip_updates=True)
