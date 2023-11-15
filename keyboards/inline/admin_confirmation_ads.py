from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

confirmation_send_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔙 Ortga', callback_data="con:back"),
            InlineKeyboardButton(text="✅ Jo'natish", callback_data="con:send")
        ]
    ]
)