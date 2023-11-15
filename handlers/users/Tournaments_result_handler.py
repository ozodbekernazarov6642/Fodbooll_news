from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageNotModified

from keyboards.inline.result_inline_keyboard import make_result_inline_button
from loader import dp
from states.main_menu_state import Tournament_state
from utils.result import team_result


@dp.callback_query_handler(Text(startswith='result'), state=Tournament_state.departments)
async def back_next_result(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    code = data.get('code')
    name = data.get('country')
    page = data.get('page')
    all_pages = data.get('all_pages')
    if call.data.split(':')[1] == '-1':
        page -= 1
        if page == 0:
            await call.answer("⚠️ Natija Topilmadi")
        if page != 0:
            await state.update_data(
                {
                    'page': page
                }
            )
    if call.data.split(":")[1] == '+1':
        if all_pages != ' ':
            if int(all_pages.split('/')[1]) <= page:
                page = page
            elif int(all_pages.split('/')[1]) > page:
                page += 1
        elif all_pages == ' ':
            page += 1

        await state.update_data(
            {
                'page': page
            }
        )
    result = await team_result(code=code, page=page)
    result = result.split(":::")
    await state.update_data(
        {
            'all_pages': result[1]
        }
    )
    button = await make_result_inline_button(per_pages=result[1])
    try:
        await call.message.edit_text(f"🔰 {name}\n\n"
                                 f"{result[0]}", reply_markup=button)
    except MessageNotModified:
        await call.answer("⚠️ Natija Topilmadi")
