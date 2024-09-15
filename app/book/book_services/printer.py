from app.book.book_services.method_interface import IBookAction
from app.book.book import Book


class BookPrinterConsole(IBookAction):
    @staticmethod
    def method(book: Book) -> None:
        print(f"Printing the book: {book.title}...\n{book.content}")


class BookPrinterReverse(IBookAction):
    @staticmethod
    def method(book: Book) -> None:
        print(f"Printing the book: {book.title}...\n{book.content[::-1]}")
