import requests
from aiogram import types

from bs4 import BeautifulSoup
from loader import bot


async def send_news(group_name):
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
    soup = BeautifulSoup(src, 'html.parser')
    count = 0
    results = []
    all_href = soup.findAll(class_='news-list-item')
    for item in all_href:
        image = item.findNext(class_='news-summary-block')
        image_ = image('img')
        image_1 = image_[0]['src']
        link = item.findNext(class_='main-link')
        title = link.text
        title_link = link.get('href')
        description = item.findNext(class_='summary')
        description_text = description.text
        count += 1
        results.append(
            {
                'id': f"photo{count}",
                'photo_url': f'https://championat.asia{image_1}',
                'thumb_url': f"https://championat.asia{image_1}",
                'title': title,
                'title_link': title_link,
                'url': f'https://championat.asia{title_link}',
                'description': description_text
            }
        )

    inline_result = []
    for result in results:
        inline_result.append(
            types.InlineQueryResultArticle(
                id=result['id'],
                title=result['title'],
                input_message_content=types.InputTextMessageContent(
                    message_text=f'<a href="https://championat.asia{result["title_link"]}">{result["title"].upper()}</a>\n\n'
                                 f"{result['description']}",
                    parse_mode='HTML'
                ),
                url=result['url'],
                thumb_url=result['photo_url'],
                description=result['description']
            )
        )
    return inline_result


# if __name__ == "__main__":
#     import requests
#     from aiogram import types
#     from aiogram.types import InlineQueryResultPhoto
#     from bs4 import BeautifulSoup
#     from loader import bot
#
#     url = 'https://championat.asia/oz/news/'
#
#     headers = {
#         'Accept': '*/*',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
#     }
#
#     req = requests.get(url, headers=headers)
#     src = req.text
#
#     file = open("index.html", "w", encoding="utf-8")
#     file.write(src)
#     file.close()
#
#     file = open("index.html", "r", encoding="utf-8")
#     src = file.read()
#     all_head = []
#     soup = BeautifulSoup(src, 'lxml')
#     count = 0
#     results = []
#     all_href = soup.findAll(class_='news-list-item')
#     for item in all_href:
#         image = item.findNext(class_='news-summary-block')
#         image_ = image('img')
#         image_1 = image_[0]['src']
#         link = item.findNext(class_='main-link')
#         title = link.text
#         title_link = link.get('href')
#         description = item.findNext(class_='summary')
#         description_text = description.text
#         count += 1
#         results.append(
#             {
#                 'id': f"photo{count}",
#                 'photo_url': f'https://championat.asia{image_1}',
#                 'thumb_url': f"https://championat.asia{image_1}",
#                 'title': f'<a href="https://championat.asia{title_link}">{title}(</a>)',
#                 'url': f'https://championat.asia{title_link}',
#                 'description': description_text
#             }
#         )
#
#     inline_result = []
#     for result in results:
#         inline_result.append(
#             types.InlineQueryResultArticle(
#                 id=result['id'],
#                 title=result['title'],
#                 input_message_content=types.InputTextMessageContent(
#                     message_text=f"{result['title']}\n"
#                                  f"{result['description']}"
#                 ),
#                 url=result['url'],
#                 thumb_url=result['photo_url'],
#                 description=result['description']
#             )
#         )
#     print(inline_result)
#
#     # Handle inline queries and send the results using the bot object
#     # Add your code here to handle inline queries and send the results
