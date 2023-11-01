from abc import ABC, abstractmethod

from app.book import Book


class DisplayBook(ABC):
    @staticmethod
    @abstractmethod
    def display(book: Book) -> None:
        pass


class ConsoleDisplay(DisplayBook):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayBook):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])


def display_book(book: Book, method_type: str) -> None:
    if method_type == "console":
        ConsoleDisplay.display(book)
    elif method_type == "reverse":
        ReverseDisplay.display(book)
    else:
        raise ValueError(f"Unknown display type: {method_type}")
