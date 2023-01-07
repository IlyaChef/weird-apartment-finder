from flask_sqlalchemy import SQLAlchemy
from db import Base,engine
from sqlalchemy import Column, Integer, String, Date

db = SQLAlchemy()

class Apartments(Base):
    __tablename__ = 'Apartments'
    cian_id = db.Column(db.Integer, primary_key=True, unique=True)
    rooms = db.Column(db.Integer, nullable=True)
    metro = db.Column(db.String, nullable=True)
    address = db.Column(db.Text, nullable=True)
    area = db.Column(db.String, nullable=True)
    house = db.Column(db.String, nullable=True)
    price = db.Column(db.Integer, nullable=True)
    description = db.Column(db.Text, nullable=True)
    renovation = db.Column(db.String, nullable=True)

def __repr__(self):
    return '<Apartments {}>'.format(self.cian_id)

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
