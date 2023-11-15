from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.back_inline_keyboard import back
from states.main_menu_state import Main_State
from loader import dp, db


# Qidiruv tugmasiga masul hendler
@dp.callback_query_handler(text='main:search', state=Main_State.user_main)
async def search_1(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("🔰Sevimli jamoangiz nomini yozing. \n\n"
                              "‼️Eslatma! Jamoa nomini imlo xatolarsiz yozilishiga e'tibor bering\n\n",
                              reply_markup=back)


# @dp.message_handler(state=Main_State.search)
# async def search_2(message: types.Message):
#     await send_news(message.text, message.from_user.id)