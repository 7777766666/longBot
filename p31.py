from aiogram import Bot, Dispatcher, executor, types
from config import KENGURY
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
import hashlib

bot = Bot(token=KENGURY)
dispatcher = Dispatcher(bot=bot)
cb = CallbackData("ikb", "action")
async def start777(_):
    print("KENGURY")

ikb = InlineKeyboardMarkup(row_width=1)
b1 = InlineKeyboardButton(text="Button 1", callback_data=cb.new("b1"))  #словарь - актион(ключ): значение
b2 = InlineKeyboardButton(text="Button 2", callback_data=cb.new("b2"))


ikb.add(b1).add(b2)

def get_ikb() -> InlineKeyboardMarkup:
    return ikb


@dispatcher.message_handler(commands=["s"])
async def start1(mes: types.Message) -> None:
    await mes.answer(text="Welcome to our telegram bot",
                     reply_markup=get_ikb())


@dispatcher.callback_query_handler(cb.filter(action="b1"))
async def push_b1(call: types.CallbackQuery) -> None:
    await call.answer(text="Hello")


@dispatcher.callback_query_handler(cb.filter(action="b2"))
async def push_b2(call: types.CallbackQuery) -> None:
    await call.answer(text="World")


@dispatcher.inline_handler()
async def in_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or "Echo" #текст от пользователя
    input_content = InputTextMessageContent(text)   #формируем контент ответного сообщения
    result_id: str = hashlib.md5(text.encode()).hexdigest() # сделали уникальный id результата
    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title="Inline Echo Mode",
    )

    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item],
                                  cache_time=1)

# @dispatcher.callback_query_handler(lambda callback_query: callback_query.data.startswith("b"))
# async def sss(callback: types.CallbackQuery) -> None:
#     if callback.data.__eq__("b1"):
#         await callback.answer("Hello")
#         # callback.answer(text="Hello")
#     elif callback.data.__contains__("b2"):
#         await callback.answer(text="World")
#     else:
#         print("lol ")




if __name__ == "__main__":
    executor.start_polling(on_startup = start777, skip_updates = True, dispatcher = dispatcher)

