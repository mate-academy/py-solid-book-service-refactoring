from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.main import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: "Book") -> None:
        pass


class ConsoleDisplay(Display):
    def display(self, book: "Book") -> None:
        print(book.content)


class ReverseDisplay(Display):
    def display(self, book: "Book") -> None:
        print(book.content[::-1])
