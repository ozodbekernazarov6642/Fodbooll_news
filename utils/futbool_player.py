import requests

from bs4 import BeautifulSoup


async def players_info(code):
    req = ''
    if code == '49':
        url = f'https://championat.asia/oz/players/c?stage=49'

        headers = {
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
        }
        req = requests.get(url, headers=headers)

    if code != '49':
        url = f'https://championat.asia/oz/players/s?stage={code}&sort=goals'

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
    # BeautifulSoup orqali HTML kodingizni tahlil qiling
    soup = BeautifulSoup(src, 'html.parser')

    # tbody ichidagi tr elementlarini tanlang
    players = soup.select('tbody tr')
    players_ = []
    for player in players:
        # Fudbolchi haqida ma'lumotlarni izlab oling
        rank = player.select_one('td.center span.rank').text.strip()
        name = player.select_one('td:nth-child(2)').text.strip()
        team = player.select_one('td:nth-child(3) img')['alt'].strip()
        goals = player.select_one('td:nth-child(4)').text.strip()

        players_.append(f"<i>{rank}</i> 👉 <b>{name}</b> - <b>{team}</b> - <b>{goals}</b>")
    return '\n\n'.join(players_)

# if __name__ == "__main__":
# from bs4 import BeautifulSoup
#
# url = f'https://championat.asia/oz/players/s?stage=885640&sort=goals'
#
# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
# }
#
# req = requests.get(url, headers=headers)
# src = req.text
#
# file = open("index.html", "w", encoding="utf-8")
# file.write(src)
# file.close()
#
# file = open("index.html", "r", encoding="utf-8")
# src = file.read()
# # BeautifulSoup orqali HTML kodingizni tahlil qiling
# soup = BeautifulSoup(src, 'html.parser')
#
# # tbody ichidagi tr elementlarini tanlang
# players = soup.select('tbody tr')
# players_ = []
# for player in players:
#     # Fudbolchi haqida ma'lumotlarni izlab oling
#     rank = player.select_one('td.center span.rank').text.strip()
#     name = player.select_one('td:nth-child(2)').text.strip()
#     team = player.select_one('td:nth-child(3) img')['alt'].strip()
#     goals = player.select_one('td:nth-child(4)').text.strip()
#
#     # Rasm manzilini base64 dan oling va pil kutubxonasidan ishlatib rasmni ko'ring
#     img_data = player.select_one('td:nth-child(3) img')['src'].split(",")[1]
#
#     players_.append(f"{rank} - {name} - {team} - {goals}")
# print('\n'.join(players_))
