import requests

from bs4 import BeautifulSoup
from loader import bot


# async def team_result(code, page=1):
async def team_calendar(code, page=1):
    global req
    if code == '49':
        url = f'https://championat.asia/oz/games/c?stage=49&sort=calendar&page={page}&per-page=10'
        headers = {
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
        }

        req = requests.get(url, headers=headers)

    if code != '49':
        url = f'https://championat.asia/oz/games/s?stage={code}&sort=calendar&page={page}&per-page=10'
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
    team_result = []
    results = soup.find_all('tr', {'data-key': True})
    for result in results:
        time = result.find('td', class_='center')
        # Gruh nomlari
        team_name = result.find('td', class_='align-right').text.strip()
        team_2 = result.find('td', class_="align-left").text
        # Hisoblar
        scores = result.find('a', class_='load-incidents').text
        # To'plamga qo'shish
        team_result.append(f'<b>👉{team_name}</b>\n'
                           f'<i>📆{time.text[0:5]}</i> <b>|</b> <i>{time.text[5::]}</i>\n'
                           f'<b>👉{team_2.strip()}</b>')
    team_result.append(f':::{soup.find("div", class_="counter").text.strip() if soup.find("div", class_="counter") else "1/1"}')
    return '\n\n'.join(team_result)

# if __name__ == "__main__":
#     url = f'https://championat.asia/oz/games/s?stage=885919&sort=calendar&page=2&per-page=10'
#     headers = {
#         'Accept': '*/*',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
#     }
#
#     req = requests.get(url, headers=headers)
#
#     src = req.text
#
#     file = open("index.html", "w", encoding="utf-8")
#     file.write(src)
#     file.close()
#
#     file = open("index.html", "r", encoding="utf-8")
#     html_kod = file.read()
#
#     # BeautifulSoup obyekti yaratamiz
#     soup = BeautifulSoup(html_kod, 'html.parser')
#     team_result = []
#     results = soup.find_all('tr', {'data-key': True})
#     for result in results:
#         # Gruh nomlari
#         team_name = result.find('td', class_='align-right').text.strip()
#         team_2 = result.find('td', class_="align-left").text
#         # Hisoblar
#         scores = result.find('a', class_='load-incidents').text
#         # To'plamga qo'shish
#         team_result.append(f'👉 <b>{team_name}</b> <i>{scores}</i> <b>{team_2.strip()}</b>')
#     team_result.append(f':::{soup.find("div", class_="counter").text.strip()}')
#     print(team_result)
