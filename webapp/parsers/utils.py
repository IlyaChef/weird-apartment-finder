import requests

from webapp.db import db
from webapp.model import Ads

def get_html(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0'
    }
    try:
        result = requests.get(url, headers = headers)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

def save_ads(title, url, published):
    ads_exists = News.query.filter(News.url == url).count()
    if not ads_exists_exists:
        ads_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()