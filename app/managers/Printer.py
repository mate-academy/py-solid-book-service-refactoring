from abc import ABC, abstractmethod
from app.managers import Book


class PrintBasic(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class PrintConsole(PrintBasic):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(PrintBasic):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content[::-1])
