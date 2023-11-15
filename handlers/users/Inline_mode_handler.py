import requests
from aiogram import types
from bs4 import BeautifulSoup
from states.main_menu_state import Main_State
from utils.search_group import send_news
from loader import dp


@dp.inline_handler()
@dp.inline_handler(state=Main_State.all_states)
async def send_news_(query: types.InlineQuery):
    text = str(query.query)
    result = await send_news(text)
    await query.answer(results=result)
    print(text)