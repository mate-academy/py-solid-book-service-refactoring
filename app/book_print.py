from app.abstract_classes import IBookPrint
from app.book_model import Book


class ConsoleBookPrint(IBookPrint):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReverseBookPrint(IBookPrint):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
