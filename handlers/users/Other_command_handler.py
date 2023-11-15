from aiogram import types

from data.config import GROUP
from keyboards.inline.admin_confirmation_ads import confirmation_send_button
from utils.bot_date_since import days_since
from loader import dp, db, bot
from states.main_menu_state import Main_State, Tournament_state, Complaints


@dp.message_handler(commands=['statistics'])
@dp.message_handler(commands=['statistics'], state=Main_State.all_states)
@dp.message_handler(commands=['statistics'], state=Tournament_state.all_states)
@dp.message_handler(commands=['statistics'], state=Complaints.all_states)
async def bot_statistics(message: types.Message):
    # Botning barcha foydalanuvchilar soni
    all_user = db.select_all_user()
    all_user_count = 0
    for o in all_user:
        all_user_count += 1
    # Botdagi faol foydalanuvchilarni oladi
    action_all_user = 0
    for z in all_user:
        try:
            chat_id = z[0]
            await bot.send_chat_action(chat_id, types.ChatActions.TYPING)
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

    await message.answer(f"🔰<b>Botdagi obunachilar</b> - <i>{all_user_count} ta</i>\n\n"
                         f"👉<b>Faol obunachilar soni</b> - <i>{action_all_user} ta</i>\n\n"
                         f"👉<b>Oxirgi 24 soatda qo'shilganlar soni</b> - <i>{last_24_count} ta</i>\n\n"
                         f"👉<b>Oxirgi 1 oyda qo'shilganlar soni</b> - <i>{last_24_count} ta</i>\n\n"
                         f"👉<b>Bot ishga tushganiga</b> - <i>{days} kun bo'ldi</i>\n\n")


@dp.message_handler(commands=['complaints'])
@dp.message_handler(commands=['complaints'], state=Main_State.all_states)
@dp.message_handler(commands=['complaints'], state=Tournament_state.all_states)
@dp.message_handler(commands=['complaints'], state=Complaints.all_states)
async def send_complaints(message: types.Message):
    await message.answer("<b>Taklif va shikoyatlaringizni yozing ✍🏻</b>\n\n"
                         "<i>Eslatma:</i> <b>Taklif va shikoyatlar matndan iborat bo'lishi shart!</b>")
    await Complaints.send_group.set()


@dp.message_handler(state=Complaints.send_group)
async def send_group(message: types.Message):
    text = message.text
    await message.delete()
    await bot.send_message(chat_id=GROUP[0],
                           text=f"<b>Foydalanuvchi:</b>{message.from_user.get_mention(as_html=True)}\n\n"
                                f"<i>{text}</i>")
    await Complaints.confirmation.set()
