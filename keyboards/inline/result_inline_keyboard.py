from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def make_result_inline_button(per_pages) -> InlineKeyboardMarkup:
    result_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='⏮', callback_data='result:-1'),
                InlineKeyboardButton(text=per_pages, callback_data='result:pages'),
                InlineKeyboardButton(text='⏭', callback_data='result:+1')
            ],
            [
                InlineKeyboardButton(text="🔙 Ortga", callback_data='back'),
                InlineKeyboardButton(text="🔝Bosh Menyu", callback_data='main_menu'),
            ]
        ]
    )
    return result_button
