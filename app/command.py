from abc import ABC, abstractmethod

from app.book import Book
from app.displayer import Displayer


class Command(ABC):
    @staticmethod
    @abstractmethod
    def command(displayer_method: Displayer.display, book: Book) -> None:
        ...


class DisplayCommand(Command):
    @staticmethod
    def command(displayer_method: Displayer.display, book: Book) -> None:
        displayer_method(book=book)


class PrintCommand(Command):
    @staticmethod
    def command(displayer_method: Displayer.display, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        displayer_method(book=book)


class SerializeCommand(Command):
    @staticmethod
    def command(displayer_method: Displayer.display, book: Book) -> str:
        return displayer_method(book=book)
