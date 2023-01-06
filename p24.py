from aiogram import Bot, Dispatcher, executor, types
from config import ID_BOT_LESSON3, PP777Bot, KENGURY
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboard_p24 import ikb

bot = Bot(KENGURY)
dp = Dispatcher(bot)

is_voted = False
async def start777(_):
    print("start !!!")


@dp.message_handler(commands="s")
async def get_photo(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.chat.id,

                         photo="https://pibig.info/uploads/posts/2021-06/thumbs/1623997495_14-pibig_info-p-priroda-solntse-priroda-krasivo-foto-16.jpg",
                         caption="Kак тебе фотка?",
                         reply_markup=ikb)

@dp.callback_query_handler(text="close")
async def ikb_close1(callback: types.CallbackQuery) -> None:
    await callback.message.delete()


@dp.callback_query_handler()
async def ikb_del1(callback: types.CallbackQuery) -> None:
    global is_voted
    if not is_voted:
        if callback.data == "like":
            await callback.answer(show_alert=False, text="Я знал, что тебе понраиться!")
            is_voted = True
        await callback.answer(show_alert=False, text="Ясно дело, что не понравится такое(((")
        is_voted = True
    await callback.answer("Ты же уже отдал свой голос!", show_alert=True)



if __name__ == "__main__":
    executor.start_polling(dp, on_startup=start777, skip_updates=True)
