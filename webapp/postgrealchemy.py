import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

df = pd.read_excel('/Users/ilyaromanov89gmail.com/projects/diploma_project/weird_apartment_finder/static/cian_base1.xlsx')

#engine = create_engine('postgresql://cqdiqzza:iFkFWOZp3T6CIKaOWkfiI84t9SJefz_y@mouse.db.elephantsql.com:5432/cqdiqzza')
#df.to_sql('Apartments_cian', con=engine)

engine = create_engine('sqlite:///apartments_cian.db')
df.to_sql('Apartments_cian', engine, if_exists='replace')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
