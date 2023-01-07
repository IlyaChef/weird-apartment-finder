import csv

from db import db_session
from model import Apartments

def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['cian_id', 'rooms','metro','address','area',
                  'house','price','description','renovation']
        reader = csv.DictReader(f, fields, delimiter=';')
        for row in reader:
            save_apartments_data(row)

def save_apartments_data(row):
    apartments = Apartments(cian_id=row['cian_id'], rooms=row['rooms'],
            metro=row['metro'], address=row['address'],
            area=row['area'], house=row['house'],
            price=row['price'], description=row['description'],
            renovation=row['renovation'])
    db_session.add(apartments)
    db_session.commit()

if __name__ == '__main__':
    read_csv('/Users/ilyaromanov89gmail.com/projects/diploma_project/weird_apartment_finder/static/cian_base_db_load.csv')