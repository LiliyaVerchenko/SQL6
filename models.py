import sqlalchemy as sq
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import func
engine = sq.create_engine('postgresql+psycopg2://postgres:Shitko77$@localhost:5432/book')
connection = engine.connect()
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)

Base = declarative_base()
class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)
    book = relationship('Book', backref='publisher')

class Book(Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'))

class Shop(Base):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)
    stocks = relationship('Stock')

class Stock(Base):
    __tablename__ = 'stock'
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), primary_key=True)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), primary_key=True)
    count = sq.Column(sq.Integer)

publ_input = int(input('Введите идентификатор целевого издателя '))
if __name__ == '__main__':
    session = Session()
    shop_list = session.query(Shop.name).join(Stock).join(Book).join(Publisher).filter(Publisher.id == publ_input).all()
    print(shop_list)
