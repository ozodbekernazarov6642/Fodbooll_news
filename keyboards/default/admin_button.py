from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

admin_main_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🆔Foydalanuvchilarning ID ni olish'),
            KeyboardButton(text="Foydalanuvchilarga Xabar yuborish📤")
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)
