import hashlib

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import InlineQuery, InlineQueryResult, InputTextMessageContent, InlineQueryResultArticle
from config import KENGURY
hashlib


bot = Bot(KENGURY)
dispatcher = Dispatcher(bot = bot)

user_data = ""

# async def start777(_):
#     print("KENGURY")

@dispatcher.message_handler(commands=["s"])
async def lol(mess: types.Message) -> None:
    await mess.answer(text="Enter number")


@dispatcher.message_handler()
async def text_h(mess: types.Message) -> None:
    global user_data
    user_data = mess.text
    await mess.reply(text="your data is save")


@dispatcher.inline_handler()
async def inl_query17(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or "Echo"
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    input_content = InputTextMessageContent(f"<b>{text} - {user_data}</b>",
                                            parse_mode="html")

    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title="Echo bot",
        description="Hello I am not east echo bot",
    )

    await bot.answer_inline_query(results=[item],
                                  inline_query_id=inline_query.id,
                                  cache_time=1)





if __name__ == "__main__":
    executor.start_polling(dispatcher=dispatcher, skip_updates=True)