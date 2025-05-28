from abc import ABC

from app.book import Book


class Print(ABC):
    def print_book(self, book: Book) -> None:
        pass


class PrintRight(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
