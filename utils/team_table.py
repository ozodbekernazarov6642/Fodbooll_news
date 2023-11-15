import requests

from bs4 import BeautifulSoup


async def team_info(code):
    # O'zbekistonni aniqlash uchun
    if code == '49':
        url = f'https://championat.asia/oz/countries/c?id=1000001'

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

        soup = BeautifulSoup(src, 'html.parser')

        # Har bir jamoa uchun malumotni chiqarish
        teams = soup.find_all('tr', {'data-key': True})
        team_table = []
        for team in teams:
            rank = team.find('span', class_='rank').text
            name = team.find('td', class_='center').find_next('td').text.strip()
            stats = [td.text.strip() for td in team.find_all('td', class_='center')[1:5]]
            last_value = team.find_all('td', class_='center')[-2].text
            team_table.append(f"<i>{rank}</i> 👉 <b>{name} - {'-'.join(stats)}-{last_value}</b>")
        return '\n\n'.join(team_table)
    if code != '49':
        url = f'https://championat.asia/oz/tables/s?stage={code}&sort=normal'

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
        soup = BeautifulSoup(src, 'html.parser')
        # Har bir jamoa uchun malumotni chiqarish
        team_table = []
        teams = soup.find_all('tr', {'data-key': True})
        for team in teams:
            rank = team.find('span', class_='rank').text
            name = team.find('td', class_='center').find_next('td').text.strip()
            stats = [td.text.strip() for td in team.find_all('td', class_='center')[1:5]]
            last_value = team.find_all('td', class_='center')[9].text.strip()
            team_table.append(f"<i>{rank}</i> 👉 <b>{name} - {'-'.join(stats)}-{last_value}</b>")
        return '\n\n'.join(team_table)

# if __name__ == '__main__':
# from bs4 import BeautifulSoup
#
# import requests
#
# from bs4 import BeautifulSoup
#
# url = f'https://championat.asia/oz/countries/c?id=1000001'
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
#
# soup = BeautifulSoup(src, 'html.parser')
#
# # Har bir jamoa uchun malumotni chiqarish
# teams = soup.find_all('tr', {'data-key': True})
# team_table = []
# for team in teams:
#     rank = team.find('span', class_='rank').text
#     name = team.find('td', class_='center').find_next('td').text.strip()
#     stats = [td.text.strip() for td in team.find_all('td', class_='center')[1:5]]
#     last_value = team.find_all('td', class_='center')[-2].text
#
#     team_table.append(f"{rank} - {name} - {'-'.join(stats)} {last_value}")
# print(team_table)
