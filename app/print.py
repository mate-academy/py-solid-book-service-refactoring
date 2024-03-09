from abc import abstractmethod, ABC

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.main import Book


class BookPrint(ABC):
    @abstractmethod
    def __init__(self, book: "Book") -> None:
        self.book = book

    @abstractmethod
    def print(self) -> None:
        pass


class ConsoleBookPrint(BookPrint):
    def __init__(self, book: "Book") -> None:
        super().__init__(book)

    def print(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class ReverseBookPrint(BookPrint):
    def __init__(self, book: "Book") -> None:
        super().__init__(book)

    def print(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])
