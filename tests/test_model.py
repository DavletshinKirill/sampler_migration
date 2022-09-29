from unittest import TestCase
from app import create_app, db
from app.fake import add_data
from app.model import Book


class TestApp(TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exist(self):
        self.assertFalse(self.app_context is None)

    def test_db_data(self):
        add_data()
        amount_books = len(Book.query.filter_by().all())
        self.assertTrue(amount_books > 10)

    def test_add_data(self):
        book = Book(name="Kirill", title="War and Piece")
        db.session.add(book)
        db.session.commit()
        self.assertTrue(Book.query.filter_by(name="Kirill").first())
