import hashlib

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineQuery


from config import KENGURY

bot888 = Bot(token=KENGURY)
dispatcher = Dispatcher(bot=bot888)


async def start777(_):
    print("KENGURY")


# @dispatcher.inline_handler(lambda query: query.query == "photo")
# async def return_photo(inline_query: types.InlineQuery) -> None:
#     text = "This is photo"
#     input_content = InputTextMessageContent(text)
#     resalt_id = str = hashlib.md5(text.encode()).hexdigest()
#     item = InlineQueryResultArticle(
#         input_message_content=input_content,
#         id = resalt_id,
#         title="lol"
#     )


@dispatcher.inline_handler()
async def in_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or "Echo empty"
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    input_content = InputTextMessageContent(text)

    if text.__eq__("photo"):
        input_content = InputTextMessageContent("!!!This is a photo!!!")

    item = InlineQueryResultArticle(
        id=result_id,
        input_message_content=input_content,
        title=text,
    )


    await bot888.answer_inline_query(inline_query_id=inline_query.id,
                                     results=[item])




if __name__ == "__main__":
    executor.start_polling(dispatcher=dispatcher, skip_updates=True, on_startup=start777)