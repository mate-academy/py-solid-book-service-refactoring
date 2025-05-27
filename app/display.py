from abc import ABC, abstractmethod
from .book import Book


class BookDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class DisplayFactory:
    @staticmethod
    def create_display(display_type: str) -> BookDisplay:
        if display_type == "console":
            return ConsoleDisplay()
        elif display_type == "reverse":
            return ReverseDisplay()
        else:
            raise ValueError(f"Unknown display type: {display_type}")
