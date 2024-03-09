from abc import ABC, abstractmethod

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.main import Book


class BookDisplay(ABC):
    @abstractmethod
    def __init__(self, book: "Book") -> None:
        self.book = book

    @abstractmethod
    def display(self) -> None:
        pass


class ConsoleBookDisplay(BookDisplay):
    def __init__(self, book: "Book") -> None:
        super().__init__(book)

    def display(self) -> None:
        print(self.book.content)


class ReverseBookDisplay(BookDisplay):
    def __init__(self, book: "Book") -> None:
        super().__init__(book)

    def display(self) -> None:
        print(self.book.content[::-1])
