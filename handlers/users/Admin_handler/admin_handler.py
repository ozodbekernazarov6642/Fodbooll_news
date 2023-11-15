import time

from aiogram.types import InputFile
from openpyxl import Workbook
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.exceptions import CantParseEntities, BadRequest

from data.config import ADMINS
from keyboards.default.admin_button import admin_main_button
from keyboards.inline.admin_confirmation_ads import confirmation_send_button
from loader import dp, bot, db
from states.Admin_state import admin_state

workbook = Workbook()
user_info = workbook.active


@dp.message_handler(CommandStart(), user_id=ADMINS)
@dp.message_handler(CommandStart(), state=admin_state.all_states, user_id=ADMINS)
async def start_admin(message: types.Message):
    await message.answer("Assalomu aleykum xurmatli Admin !", reply_markup=admin_main_button)


@dp.message_handler(text='🆔Foydalanuvchilarning ID ni olish', user_id=ADMINS)
@dp.message_handler(text='🆔Foydalanuvchilarning ID ni olish', state=admin_state.all_states, user_id=ADMINS)
async def ads_button_admin(message: types.Message):
    all_user = db.select_all_user()
    for z in range(0, len(all_user)):
        user_info[f"A1"] = "Id"
        user_info[f"B1"] = "Username"
        user_info[f"C1"] = "First_name"
        user_info[f"A{z + 2}"] = all_user[z][0]
        user_info[f"B{z + 2}"] = all_user[z][2]
        user_info[f"C{z + 2}"] = all_user[z][3]
    for z in range(0, len(all_user)):
        try:
            chat_id = all_user[z][0]
            await bot.send_chat_action(chat_id, types.ChatActions.TYPING)
            user_info[f"EK{z+1}"] = all_user[z][0]
        except:
            pass

    workbook.save("user_info.xlsx")
    await message.answer_document(InputFile(path_or_bytesio="user_info.xlsx"))
