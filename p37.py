from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import KENGURY
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

storage = MemoryStorage()
bot = Bot(KENGURY)
dp = Dispatcher(bot, storage=storage)


class ProfileStatesGroup(StatesGroup):
    photo = State()
    name = State()
    age = State()
    description = State()

def get_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("/create"))
    return kb


async def start777(_):
    print("KENGURY")


@dp.message_handler(commands=["s"])
async def cmd_start(mess: types.Message) -> None:
    await mess.answer(text="welcome, enter your name /create",
                      reply_markup=get_kb())


@dp.message_handler(commands=["create"])
async def cmd_create(mess: types.Message) -> None:
    await mess.reply(text="Давайте оформим Ваш профиль. Пришлит своё фото.")
    await ProfileStatesGroup.photo.set()    #устанавливаем состояние на ожидание фото

@dp.message_handler(content_types=["photo"], state=ProfileStatesGroup.photo)
async def load_photo(mess: types.Message, state:FSMContext) -> None:
    async with state.proxy() as data:
        data["photo"] = mess.photo[0].file_id

    await mess.reply(text="Как Ваше имя?")
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.name)
async def load_name(mess: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["name"] = mess.text

    await mess.answer(text="Сколько Вам лет?")
    await ProfileStatesGroup.next()


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
                             caption=f"{data['name']}, {data['age']}\n{data['description']} ")

    await mess.reply(text="Спасибо, Ваш профиль полностью заполнен!")
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=start777, skip_updates=True)

