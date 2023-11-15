from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

tournaments_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿O'zbekiston", callback_data='country:49')
        ],
        [
            InlineKeyboardButton(text="🏴󠁧󠁢󠁥󠁮󠁧󠁿Angliya", callback_data='country:885640'),
            InlineKeyboardButton(text="🇪🇸Ispanya", callback_data='country:886037')
        ],
        [
            InlineKeyboardButton(text='🇩🇪Germanya', callback_data='country:885904'),
            InlineKeyboardButton(text='🇮🇹Italya', callback_data='country:885919')
        ],
        [
            InlineKeyboardButton(text="🇫🇷Fransiya", callback_data='country:885801'),
            InlineKeyboardButton(text='🇷🇺Rassiya', callback_data='country:886123')
        ],
        [
            InlineKeyboardButton(text="🇸🇦Saudiya Arabistoni", callback_data='country:886553')
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="country:back")
        ]

    ]
)


tournaments_sub_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Jadval', callback_data="tournament:table"),
            InlineKeyboardButton(text="Natija", callback_data="tournament:result")
        ],
        [
            InlineKeyboardButton(text='Taqvim', callback_data="tournament:calendar"),
            InlineKeyboardButton(text="Futbolchilar", callback_data="tournament:goals")
        ],
        [
            InlineKeyboardButton(text="🔙Ortga", callback_data="tournament:back")
        ]
    ]
)