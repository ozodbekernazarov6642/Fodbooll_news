from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔙 Ortga', callback_data="back")
        ],
        [
            InlineKeyboardButton(text="🔝Bosh Menyu", callback_data="main_menu")
        ]
    ]
)
