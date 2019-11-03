from bs4 import BeautifulSoup
import requests
from time import sleep
import urllib.parse

sleep(3)


class NewsParser:

    def __init__(self, url, searching_text):

        self.url = url
        self.headers = None
        self.search_request = None
        self.params = None
        self.resp = None
        self.links = None

        self.set_params(searching_text)

    def set_params(self, searching_text):

        searching_text = searching_text

        self.headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml',
            'Accept-Encoding': 'gzip, deflate, br',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15(KHTML, like Gecko) Version / 13.0.2 Safari / 605.1.15',
            'Connection': 'keep-alive'
        }

        self.params = {

            'text': searching_text,
            'rpt': 'nnews2',
            'grhow': 'clutop',
            'rel': 'rel'


        }

        '''
        {
            'wiz_no_news': 1,
            'within': 777,
            'from_day': 28,
            'from_month': 10,
            'from_year': 2019,
            'to_day': 1,
            'to_month': 11,
            'to_year': 2019
        }
        '''
        return self.params

    def navigate_url(self):
        r=requests.get(self.url, headers=self.headers, params=self.params)
        self.resp = r
        return self.resp

    def collect_news_links(self):
        html=self.resp.text
        soup = BeautifulSoup(html, 'lxml')
        self.links=[x.find('a').get('href') for x in soup.find_all('h2')]
        return self.links

    def parse_news(self, html):
        pass

    def save_news(self):
        pass


class YANewsParser(NewsParser):
    pass

class RBCNewsParser(NewsParser):
    pass