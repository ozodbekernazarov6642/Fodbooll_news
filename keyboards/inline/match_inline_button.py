import requests
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bs4 import BeautifulSoup
from loader import bot


async def match_inline(group_name):
    url = f'https://championat.asia/oz/news/search?q={group_name}'

    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }

    req = requests.get(url, headers=headers)
    src = req.text

    file = open("index.html", "w", encoding="utf-8")
    file.write(src)
    file.close()

    file = open("index.html", "r", encoding="utf-8")
    src = file.read()
    all_head = []
    soup = BeautifulSoup(src, 'lxml')



