from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile

from keyboards.inline.calendar_inline_button import make_calendar_inline_button
from utils.calendar import team_calendar
from utils.result import team_result
from keyboards.inline.back_inline_keyboard import back
from keyboards.inline.tournaments_inline_keyboard import tournaments_inline, tournaments_sub_inline
from states.main_menu_state import Main_State, Tournament_state
from utils.futbool_player import players_info
from loader import dp, db
from utils.team_table import team_info
from keyboards.inline.result_inline_keyboard import make_result_inline_button


# turnirlar tugmasiga masul hendler
@dp.callback_query_handler(text='main:tournaments', state=Main_State.user_main)
async def tournaments_1(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="Turnirni tanlang👇", reply_markup=tournaments_inline)
    await Main_State.Tournaments.set()


@dp.callback_query_handler(Text(startswith='country'), state=Main_State.Tournaments)
async def country(call: types.CallbackQuery, state: FSMContext):
    country_name = ''
    country_code = call.data.split(':')[1]
    if country_code == '49':
        country_name = "🇺🇿O'zbekiston"
    elif country_code == '885640':
        country_name = "🏴󠁧󠁢󠁥󠁮󠁧󠁿Angliya"
    elif country_code == '886037':
        country_name = "🇪🇸Ispanya"
    elif country_code == '885904':
        country_name = "🇩🇪Germanya"
    elif country_code == '885919':
        country_name = "🇮🇹Italya"
    elif country_code == '885801':
        country_name = "🇫🇷Fransiya"
    elif country_code == '886123':
        country_name = "🇷🇺Rassiya"
    elif country_code == '886553':
        country_name = "🇸🇦Saudiya Arabistoni"
    await state.update_data(
        {
            "code": country_code,
            "country": country_name.upper(),
            "page": 1,
            "all_pages": " "
        }
    )
    await call.message.delete()
    await call.message.answer(text="Turnir Bo'limini tanlang👇", reply_markup=tournaments_sub_inline)
    await Tournament_state.liga.set()


@dp.callback_query_handler(text='tournament:goals', state=Tournament_state.liga)
async def info_players(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    emoji = await call.message.answer_sticker(sticker=InputFile(path_or_bytesio='data/emoji/AnimatedSticker.tgs'))
    data = await state.get_data()
    code = data.get('code')
    name = data.get('country')
    info = await players_info(code)
    await call.message.answer(f"🔰 {name}\n\n{info}", reply_markup=back)
    await emoji.delete()
    await Tournament_state.departments.set()


@dp.callback_query_handler(text="tournament:table", state=Tournament_state.liga)
async def info_team(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    emoji = await call.message.answer_sticker(sticker=InputFile(path_or_bytesio='data/emoji/AnimatedSticker.tgs'))
    data = await state.get_data()
    code = data.get('code')
    name = data.get('country')
    info = await team_info(code)
    await call.message.answer(f"🔰 {name}\n\n"
                              f"<i>T/r</i>      <b>Jamoa nomi</b>   <b>O'-Yu-D-M-O</b> \n\n"
                              f"{info}", reply_markup=back)
    await emoji.delete()
    await Tournament_state.departments.set()


@dp.callback_query_handler(text='tournament:result', state=Tournament_state.liga)
async def result_team(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    emoji = await call.message.answer_sticker(sticker=InputFile(path_or_bytesio='data/emoji/AnimatedSticker.tgs'))
    data = await state.get_data()
    code = data.get('code')
    name = data.get('country')

    result = await team_result(code=code)
    result = result.split(":::")
    button = await make_result_inline_button(per_pages=result[1])
    await call.message.answer(f"🔰 {name}\n\n"
                              f"{result[0]}", reply_markup=button)
    await emoji.delete()
    await Tournament_state.departments.set()


@dp.callback_query_handler(text='tournament:calendar', state=Tournament_state.liga)
async def calendar_team(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    emoji = await call.message.answer_sticker(sticker=InputFile(path_or_bytesio='data/emoji/AnimatedSticker.tgs'))
    data = await state.get_data()
    code = data.get('code')
    name = data.get('country')

    result = await team_calendar(code=code)
    result = result.split(":::")
    button = await make_calendar_inline_button(per_pages=result[1])
    await call.message.answer(f"🔰 {name}\n\n"
                              f"{result[0]}", reply_markup=button)
    await emoji.delete()
    await Tournament_state.departments.set()
