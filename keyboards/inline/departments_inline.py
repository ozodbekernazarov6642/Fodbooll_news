from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

departments_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Qidiruv🔎", switch_inline_query_current_chat='')
        ],
        [
            InlineKeyboardButton(text="Turnirlar", callback_data="main:tournaments"),
            InlineKeyboardButton(text="MatchCenter(Live)", callback_data="main:live")
        ],
        [
            InlineKeyboardButton(text="🔙Ortga", callback_data="main:back")
        ]
    ]
)

