from abc import ABC, abstractmethod

from app.models import Book


class DisplayContent(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplayContent(DisplayContent):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayContent(DisplayContent):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
