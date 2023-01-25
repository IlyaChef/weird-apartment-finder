from datetime import datetime, timedelta
import locale
import platform

from bs4 import BeautifulSoup

from webapp import db
from webapp.model import Ads
from webapp.utils import get_html, save_ads

if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL, "russian")
else:
    locale.setlocale(locale.LC_TIME, 'ru_RU')

def parse_avito_date(date_str):
    if 'сегодня' in date_str:
        today = datetime.now()
        date_str = date_str.replace('сегодня', today.strftime('%d %B %Y'))
    elif 'вчера' in date_str:
        yesterday = datetime.now() - timedelta(days=1)
        date_str = date_str.replace('вчера', yesterday.strftime('%d %B %Y'))
    try:
        return datetime.strptime(date_str, '%d %B %Y в %H:%M')
    except ValueError:
        return datetime.now()

def get_avito_snippets():
    html = get_html("https://www.avito.ru/moskva/kvartiry/prodam-ASgBAgICAUSSA8YQ?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKk5NLErOcMsvyg3PTElPLVGyrgUEAAD__xf8iH4tAAAA&f=ASgBAQICAUSSA8YQAUDKCKSKWZqsAZisAZasAZSsAYhZhlmEWYJZgFk")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_ads = soup.find('div', class_='items-items-kAJAg').findAll('div', id_='iva-item-root')
        for ads in all_ads:
            title = ads.find('a', class_='iva-item-sliderLink-uLz1v').text
            url = ads.find('a', class_='link-link-MbQDP')['href']
            published = ads.find('span', class_='tm-article-snippet__datetime-published').text
            published = parse_avito_date(published)
            print(title, url, published)

def get_avito_content():
    ads_without_text = Ads.query.filter(Ads.text.is_(None))
    for ads in ads_without_text:
        html = get_html(ads.url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            article = soup.find('div', class_='pull-down').decode_contents()
            if article:
                ads.text = article
                db.session.add(news)
                db.session.commit()