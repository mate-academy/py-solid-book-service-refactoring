from abc import ABC, abstractmethod

from .book import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(Display):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class BookDisplayer:
    @staticmethod
    def display(book: Book, display_type: str) -> None:
        if display_type == "console":
            ConsoleDisplay().display(book)
        elif display_type == "reverse":
            ReverseDisplay().display(book)
        else:
            raise ValueError(f"Unknown display type: {display_type}")
