from abc import ABC, abstractmethod

from app.models import Book


class DisplayContent(ABC):
    @staticmethod
    @abstractmethod
    def display_content(book: Book) -> None:
        pass


class DisplayInConsole(DisplayContent):
    @staticmethod
    def display_content(book: Book) -> None:
        print(book.content)


class DisplayToReversed(DisplayContent):
    @staticmethod
    def display_content(book: Book) -> None:
        print(book.content[::-1])
