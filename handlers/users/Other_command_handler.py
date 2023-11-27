import time
from keyboards.default.main_menu_button import main_keyboard
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, InputFile
from keyboards.default.admin_button import admin_main_button
from data.config import GROUP
from keyboards.inline.admin_confirmation_ads import confirmation_send_button
from utils.bot_date_since import days_since
from loader import dp, db, bot
from states.main_menu_state import Main_State, Tournament_state, Complaints
from states.Admin_state import admin_state


@dp.message_handler(commands=['statistics'])
@dp.message_handler(commands=['statistics'], state=Main_State.all_states)
@dp.message_handler(commands=['statistics'], state=Tournament_state.all_states)
@dp.message_handler(commands=['statistics'], state=Complaints.all_states)
@dp.message_handler(commands=['statistics'], state=admin_state.all_states)
async def bot_statistics(message: types.Message, state: FSMContext):
    emoji = await message.answer_sticker(sticker=InputFile(path_or_bytesio='data/emoji/AnimatedSticker.tgs'))
    # Botning barcha foydalanuvchilar soni
    all_user = db.select_all_user()
    all_user_count = 0
    for o in all_user:
        all_user_count += 1
    # Botdagi faol foydalanuvchilarni oladi
    action_all_user = 0
    print(await bot.get_me())
    for z in all_user:
        try:
            await bot.send_chat_action(chat_id=z[0], action=types.ChatActions.TYPING)
            action_all_user += 1
        except:
            pass

    # Oxirgi 24 soatda qo'shilgan foydalanuvchilar
    last_24 = db.get_last_24_hours_users()
    last_24_count = 0
    for o in last_24:
        last_24_count += 1
    # Oxirgi oyda qo'shilgan foydalanuvchilar
    last_month = db.get_last_month_users()
    last_month_count = 0
    for d in last_month:
        last_month_count += 1
    # Bot ishga tushgan kunda hozirgacha
    days = await days_since()
    await emoji.delete()
    await message.answer(f"🔰<b>Botdagi obunachilar</b> - <i>{all_user_count} ta</i>\n\n"
                         f"👉<b>Faol obunachilar soni</b> - <i>{action_all_user} ta</i>\n\n"
                         f"👉<b>Oxirgi 24 soatda qo'shilganlar soni</b> - <i>{last_24_count} ta</i>\n\n"
                         f"👉<b>Oxirgi 1 oyda qo'shilganlar soni</b> - <i>{last_month_count} ta</i>\n\n"
                         f"👉<b>Bot ishga tushganiga</b> - <i>{days} kun bo'ldi</i>\n\n"
                         f"📈 | <a href='https://t.me/varfootballbot'>VarFootball</a>",
                         disable_web_page_preview=True)
    await state.finish()


@dp.message_handler(commands=['complaints'])
@dp.message_handler(commands=['complaints'], state=Main_State.all_states)
@dp.message_handler(commands=['complaints'], state=Tournament_state.all_states)
@dp.message_handler(commands=['complaints'], state=Complaints.all_states)
@dp.message_handler(commands=['complaints'], state=admin_state.all_states)
async def send_complaints(message: types.Message, state: FSMContext):
    await message.answer("<b>Taklif va shikoyatlaringizni yozing ✍🏻</b>\n\n"
                         "<i>Eslatma:</i> <b>Taklif va shikoyatlar matndan iborat bo'lishi shart!</b>",
                         disable_web_page_preview=True, reply_markup=ReplyKeyboardRemove())
    await Complaints.send_group.set()


@dp.message_handler(state=Complaints.send_group)
async def send_group(message: types.Message, state: FSMContext):
    await bot.forward_message(chat_id=GROUP[0], from_chat_id=message.chat.id, message_id=message.message_id)
    await message.delete()
    xabar = await message.answer("<b>Qo'llab-Quvvatlash gruhiga jo'natildi📤</b>")
    await state.finish()
    time.sleep(3)
    await xabar.delete()
    await message.answer("<b>Asosiy Menyuni birini tanlang👇</b>", reply_markup=main_keyboard)
