from random import randint
from sqlalchemy.exc import IntegrityError
from faker import Faker
from . import db
from .model import Book


def add_data(book_amount=11):
    faker = Faker()
    counter = 0
    while counter < book_amount:
        book = Book(name=faker.name(),
                    title=faker.text())
        db.session.add(book)
        try:
            db.session.commit()
            counter += 1
        except IntegrityError:
            db.session.rollback()
