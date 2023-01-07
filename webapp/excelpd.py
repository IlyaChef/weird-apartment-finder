import pandas as pd
from sqlalchemy import create_engine

df = pd.read_excel('/Users/ilyaromanov89gmail.com/projects/diploma_project/weird_apartment_finder/static/cian_base1.xlsx')

engine = create_engine('postgresql://cqdiqzza:iFkFWOZp3T6CIKaOWkfiI84t9SJefz_y@mouse.db.elephantsql.com:5432/cqdiqzza')
df.to_sql('Apartments_cian', con=engine)





