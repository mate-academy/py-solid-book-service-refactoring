from app.book_base import BookInitialize
from app.book_display import BookDisplay
from app.book_print import BookPrint
from app.book_serialize import BookSerialize


class Book(BookDisplay, BookPrint, BookSerialize, BookInitialize):
    pass
