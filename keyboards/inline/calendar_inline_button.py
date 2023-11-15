from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def make_calendar_inline_button(per_pages):
    calendar_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='⏮', callback_data='calendar:-1'),
                InlineKeyboardButton(text=per_pages, callback_data='calendar:pages'),
                InlineKeyboardButton(text='⏭', callback_data='calendar:+1')
            ],
            [
                InlineKeyboardButton(text="🔙 Ortga", callback_data='back'),
                InlineKeyboardButton(text="🔝Bosh Menyu", callback_data='main_menu'),
            ]
        ]
    )
    return calendar_button
