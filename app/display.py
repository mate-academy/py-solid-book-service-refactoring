from abc import ABC, abstractmethod

from app.book import Book


class DisplayBook(ABC):
    def __init__(self, book: Book):
        self.book = book

    @abstractmethod
    def display(self) -> None:
        pass


class ConsoleDisplay(DisplayBook):

    def display(self) -> None:
        print(self.book.content)


class ReverseDisplay(DisplayBook):

    def display(self) -> None:
        print(self.book.content[::-1])


def display_book(book: Book, method_type: str) -> None:
    mappings = {"console": ConsoleDisplay, "reverse": ReverseDisplay}
    displayer = mappings.get(method_type)
    if displayer:
        displayer(book).display()
    else:
        raise ValueError(f"Unknown display type: {method_type}")
