from abc import ABC, abstractmethod
from app.models import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class DisplayConsole(Display):
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayReverse(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class Print(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class PrintConsole(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
