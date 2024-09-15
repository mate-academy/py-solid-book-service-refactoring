from app.book.book_services.method_interface import IBookAction
from app.book.book import Book


class BookDisplayerConsole(IBookAction):
    @staticmethod
    def method(book: Book) -> None:
        print(book.content)


class BookDisplayerReverse(IBookAction):
    @staticmethod
    def method(book: Book) -> None:
        print(book.content[::-1])
