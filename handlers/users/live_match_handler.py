from aiogram import types
from utils.match_center import live_match
from aiogram.types import InputFile
from keyboards.inline.back_inline_keyboard import back

from states.main_menu_state import Main_State
from loader import dp, db


@dp.callback_query_handler(text='main:live', state=Main_State.user_main)
async def send_live(call: types.CallbackQuery):
    await call.message.delete()
    emoji = await call.message.answer_sticker(sticker=InputFile(path_or_bytesio='data/emoji/AnimatedSticker.tgs'))
    await call.message.answer(await live_match(), reply_markup=back)
    await emoji.delete()
    await Main_State.match_center.set()

