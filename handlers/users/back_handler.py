from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.departments_inline import departments_keyboard
from keyboards.inline.tournaments_inline_keyboard import tournaments_inline, tournaments_sub_inline
from states.main_menu_state import Main_State, Complaints
from keyboards.inline.back_inline_keyboard import back
from keyboards.default.main_menu_button import main_keyboard
from states.main_menu_state import Tournament_state
from loader import dp, db


# Asosiy Menyu tugmasiga masul hendler
@dp.message_handler(text="🏠Asosiy Menyu")
@dp.message_handler(text="🏠Asosiy Menyu", state=Main_State.all_states)
@dp.message_handler(text="🏠Asosiy Menyu", state=Tournament_state.all_states)
async def main(message: types.Message):
    await message.answer("Bo'limni tanlang 👇", reply_markup=departments_keyboard)
    await Main_State.user_main.set()


#              Asossiy manyuda turgan paytda ortga qaytish tugmasi
@dp.callback_query_handler(text='main:back', state=Main_State.user_main)
async def main_back(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Asosiy menyuni tanlang🤳", reply_markup=main_keyboard)
    await state.finish()


# Qidurv bo'limida turganda ortga qaytaruvchi
@dp.callback_query_handler(text='back', state=Main_State.match_center)
async def live_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Bo'limni tanlang 👇", reply_markup=departments_keyboard)
    await Main_State.user_main.set()


@dp.callback_query_handler(text="country:back", state=Main_State.Tournaments)
async def tournaments_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Bo'limni tanlang 👇", reply_markup=departments_keyboard)
    await Main_State.user_main.set()


@dp.callback_query_handler(text="main_menu", state=Main_State.all_states)
@dp.callback_query_handler(text="main_menu", state=Tournament_state.all_states)
async def main_menu_back(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Botdan foydalanish uchun Asosiy menyu tugmasini bosing 👇", reply_markup=main_keyboard)
    await state.finish()


@dp.callback_query_handler(text="tournament:back", state=Tournament_state.liga)
async def tournament_back(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="Turnirni tanlang👇", reply_markup=tournaments_inline)
    await Main_State.Tournaments.set()


@dp.callback_query_handler(text='back', state=Tournament_state.departments)
async def live_back(call: types.CallbackQuery, state: FSMContext):
    # state yangilash
    await state.update_data(
        {
            "page": 1,
            "all_pages": " "
        }
    )
    await call.message.delete()
    await call.message.answer(text="Turnir Bo'limini tanlang👇", reply_markup=tournaments_sub_inline)
    await Tournament_state.liga.set()



