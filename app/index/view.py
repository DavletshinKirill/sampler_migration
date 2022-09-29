from . import index
from flask import request
from ..model import Book


@index.route("/")
def index():
    return "Hello world!"
