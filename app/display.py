from abc import ABC, abstractmethod
from app.book import Book


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


def display_command(book: Book, method_type: str) -> None:
    if method_type == "console":
        method_type = ConsoleDisplay()
    elif method_type == "reverse":
        method_type = ReverseDisplay()
    else:
        raise ValueError(f"Unknown display type: {method_type}")
    method_type.display(book)
