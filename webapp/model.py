from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Apartments(db.Model):
    __tablename__ = 'Apartments'
    cian_id = db.Column(db.Integer, primary_key=True, unique=True)
    rooms = db.Column(db.String, nullable=False)
    metro = db.Column(db.String, nullable=True)
    address = db.Column(db.Text, nullable=False)
    area = db.Column(db.String, nullable=False)
    house = db.Column(db.String, nullable=False)
    price = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    renovation = db.Column(db.String, nullable=True)

def __repr__(self):
    return '<Apartments {}>'.format(self.cian_id)

