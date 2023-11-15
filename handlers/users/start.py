import datetime

import pytz
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main_menu_button import main_keyboard
from states.main_menu_state import Main_State, Tournament_state, Complaints
from loader import dp, db, bot


@dp.message_handler(CommandStart())
@dp.message_handler(CommandStart(), state=Main_State.all_states)
@dp.message_handler(CommandStart(), state=Tournament_state.all_states)
@dp.message_handler(CommandStart(), state=Complaints.all_states)
async def bot_start(message: types.Message, state: FSMContext):
    existing_user = db.select_user(message.from_user.id)
    if not existing_user:
        tz = pytz.timezone('Asia/Tashkent')
        now = datetime.datetime.now(tz)
        # Agar foydalanuvchi birinchi marta botga kirganda shu habarni yuborad
        db.add_user(
            int(message.from_user.id), str(message.from_user.username), str(message.from_user.first_name),
            now.timestamp()
        )
        await message.answer(
            f"<b>Assalomu Alaykum {message.from_user.full_name}</b> ! \n\n"
            f"🔴Bu bot orqali siz sevimli jamoangiz xaqidagi xabarlar\n"
            f"🔴Chempionatlar turnir jadvallari\n"
            f"🔴Uchrashuvlar ro'yxati xaqida \n"
            f"🔴Ma'lumotlarni kuzatib borishingiz mumkin",
            reply_markup=main_keyboard)
        await state.finish()
    # botga oldin kirgan lekin hozir /start buyrig'ini yubordi. shunda bu habar chiqadi

    if existing_user:
        await message.answer("Botdan foydalanish uchun Asosiy menyu tugmasini bosing 👇", reply_markup=main_keyboard)
        await state.finish()
