import requests

from bs4 import BeautifulSoup



async def live_match():
    url = f'https://championat.asia/oz'
    live = []
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
    html_kod = file.read()

    # BeautifulSoup obyekti yaratamiz
    soup = BeautifulSoup(html_kod, 'html.parser')

    # O'yinlar elementlari
    oyinlar = soup.find_all('a', class_='row with-icon')

    for oyin in oyinlar:
        # O'yin boshlanish vaqti
        boshlanish_vaqt = ''
        time = oyin.find('div', class_='icon')
        if time.text != '':
            boshlanish_vaq_ = oyin.find("div", class_="icon").text
            boshlanish_vaqt = f'🕔{boshlanish_vaq_.strip()}'
        if time.find('span', class_='matchcenter-sprite-finished'):
            boshlanish_vaqt = "🙅‍♂️Tugallangan"
        if time.find('span', class_='matchcenter-sprite-halftime'):
            boshlanish_vaqt = "🙋‍♂️Tanaffus"


        # Gruh nomi
        gruhlar = []
        for team in oyin.find_next('div', class_='score-cell'):
            gruh_nomi = team.findNext('span').text
            gruhlar.append(gruh_nomi)
        # Hisoblar
        hisoblar = oyin.find_all('div', class_='score')
        hisob_str = ''.join(h.text for h in hisoblar)

        # Natijani chiqaramiz
        # print(hisob_str)
        live.append(
            f'🔰{gruhlar[0].strip()} - {hisob_str.split("-")[0]}\n'
            f'{boshlanish_vaqt.strip()}\n'
            f'🔰{gruhlar[-1].strip()} - {hisob_str.split("-")[1]}\n'
            f'__________________________________________________')
    live.append('BOT linki')
    live_1 = '\n\n'.join(live)
    return live_1

# if __name__ == "__main__":
# import requests
#
# from bs4 import BeautifulSoup
# from loader import bot
#
# # async def live_match(user_id):
# url = f'https://championat.asia/oz'
# live = []
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
# html_kod = file.read()
#
# # BeautifulSoup obyekti yaratamiz
# soup = BeautifulSoup(html_kod, 'html.parser')
#
# # O'yinlar elementlari
# oyinlar = soup.find_all('a', class_='row with-icon')
#
# for oyin in oyinlar:
#     # O'yin boshlanish vaqti
#     boshlanish_vaqt = oyin.find('div', class_='icon').text
#
#     # Gruh nomi
#     gruhlar = []
#     icon_link_ = []
#     for team in oyin.find_next('div', class_='score-cell'):
#         try:
#             icon = team.find_next('div', class_='logo')('img')
#             icon_link = icon[0]['src']
#         except:
#             pass
#         gruh_nomi = team.findNext('span').text
#         gruhlar.append(gruh_nomi)
#         icon_link_.append(icon_link)
#     # Hisoblar
#     hisoblar = oyin.find_all('div', class_='score')
#     hisob_str = ' - '.join(h.text for h in hisoblar)
#
#     # Natijani chiqaramiz
#
#     live.append(
#         f'🔰{boshlanish_vaqt.strip()} {gruhlar[0].strip()}<img src="https://championat.asia{icon_link_[0]}> '
#         f'{hisob_str} <img src="https://championat.asia{icon_link_[0]}>{gruhlar[-1].strip()}')
# live_1 = '\n\n'.join(live)
