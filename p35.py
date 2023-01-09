from aiogram import Bot, Dispatcher, executor, types
from config import KENGURY
from aiogram.types import InlineQueryResult, InlineQuery, InlineQueryResultArticle
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext


storage = MemoryStorage()
bot = Bot("5930354248:AAGtL1XeJTu0P84wz-FMHZAWRKiFhajlHwk")
dp = Dispatcher(bot, storage=storage)


def get_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("Start work"))
    return kb


def get_cancel() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("/cancel"))

class ClientStatesGroup(StatesGroup):
    photo = State()
    desc = State()

async def start777(_):
    print("KENGURY")


@dp.message_handler(commands=["s"])
async def cmd_start(mess: types.Message) -> None:
    await mess.answer("Welcome",
                      reply_markup=get_kb())


@dp.message_handler(commands=["cancel"], state="*")
async def cmd_start(mess: types.Message, state: FSMContext) -> None:
    current_state= await state.get_state()
    if current_state is None:
        return

    await mess.reply(text="Отменил", reply_markup=get_kb())
    await state.finish()


@dp.message_handler(Text(equals="Start work", ignore_case=True), state=None)
async def start333(mess: types.Message) -> None:
    await ClientStatesGroup.photo.set()
    await mess.answer("send photo first",
                      reply_markup=get_cancel())


@dp.message_handler(lambda mess: not mess.photo, state=ClientStatesGroup.photo)
async def check_photo(mess: types.Message):
    return await mess.reply(text="It is not photo, lol!")


@dp.message_handler(lambda mess: types.Message, content_types=["photo"], state=ClientStatesGroup.photo)
async def load_photo(mess: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = mess.photo[0].file_id

    await ClientStatesGroup.next()
    await mess.reply("And now sen description please!")


@dp.message_handler(state=ClientStatesGroup.desc)
async def load_photo7(mess: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["desc"] = mess.text

    await mess.reply("Your photo is saved")

    async with state.proxy() as data:
        await bot.send_photo(chat_id=mess.from_user.id,
                             photo=data["photo"],
                             caption=data["desc"])

    await state.finish()





if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, on_startup=start777, skip_updates=True)