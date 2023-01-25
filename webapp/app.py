from flask import Flask
import requests
from bs4 import BeautifulSoup

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    with app.app_context():
        db.create_all()

@app.route('/')
def index():
    page = request.args.get('page', default=1, type=int)
    apartments_per_page = 20
    apartments = session.query(Apartment).offset((page-1)*apartments_per_page).limit(apartments_per_page).all()
    return render_template('index.html', apartments=apartments, page=page)

#def get_avito_html(url, page=1):
    params = {'p': page}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.text
    else:
        return None

#def get_apartment_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', class_='')
    return [link['href'] for link in links]

#def get_apartment_html(apartment_url):
    response = requests.get(apartment_url)
    if response.status_code == 200:
        return response.text
    else:
        return None

#def get_apartment_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('span', class_='___').text
    id = soup.find('div', class_='___').text
    images = [img['src'] for img in soup.find_all('img', class_='____')]
    address = soup.find('span', class_='____').text
    metro = soup.find('span', class_='____').text
    area = soup.find('span', class_='____').text
    house = soup.find('span', class_='____').text
    price = soup.find('span', class_='___').text
    description = soup.find('div', class_='____').text
    renovation = soup.find('div', class_='____').text
    return {
        'title': title,
        'id': id,
        'images': images,
        'address': address,
        'metro': metro,
        'area': area,
        'house': house,
        'price': price,
        'description': description
        'renovation': renovation
    }

#def scrape_category(url):
    apartments = []
    page = 1
    while True:
        html = get_avito_html(url, page)
        if not html:
            break
        apartment_links = get_apartment_links(html)
        for link in apartment_links:
            apartmnent_html = get_apartment_html(link)
            if not apartment_html:
                continue
            aparment = get_apartment_data(apartment_html)
            apartments.append(aparment)
        page += 1
    return apartments

if __name__ == '__main__':
    app.run(debug=True)


