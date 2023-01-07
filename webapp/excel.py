import psycopg2

from openpyxl import load_workbook

book = load_workbook(filename='/Users/ilyaromanov89gmail.com/projects/diploma_project/weird_apartment_finder/static/cian_base_final.xlsx')

sheet = book['cian_base1']

# Чтение данных в терминале:
for item in range(1, 12):
     print(sheet['A' + str(item)].value, sheet['B' + str(item)].value, sheet['C' + str(item)].value,
     sheet['D' + str(item)].value, sheet['E' + str(item)].value, sheet['F' + str(item)].value,
     sheet['G' + str(item)].value, sheet['H' + str(item)].value, sheet['I' + str(item)].value)
# Подключение к базе данных:
conn = psycopg2.connect(
     host='mouse.db.elephantsql.com',
     database='cqdiqzza',
     user='cqdiqzza',
     password='iFkFWOZp3T6CIKaOWkfiI84t9SJefz_y'
)

# Вставка данных в базу:
for row in sheet.rows:
     values = [cell.value for cell in row]

     with conn.cursor() as cur:
          cur.execute('INSERT INTO "Apartments" (cian_id, rooms, metro, address, area, house, price, description, renovation) VALUES (%(cian_id)s, %(rooms)s, %(metro)s, %(address)s, %(area)s, %(house)s, %(price)s, %(description)s, %(renovation)s)', values)


conn.commit()

conn.close()