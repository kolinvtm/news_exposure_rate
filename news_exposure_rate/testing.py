from parser import NewsParser

import requests

url = 'https://news.yandex.ru/yandsearch?'
word = 'nlmk'

news = NewsParser(url, word)

print(news.navigate_url())

print(news.collect_news_links())


# r = requests.get(url)
# print(r)



