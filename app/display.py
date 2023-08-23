from app.book import Book
from abc import ABC, abstractmethod


class BookDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class BookDisplayConsole(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class BookDisplayReverse(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class Display:
    display_types = {
        "console": BookDisplayConsole,
        "reverse": BookDisplayReverse}

    def display_book(self, display_type: str, book: Book) -> str:
        if display_type in self.display_types:
            return self.display_types[display_type]().display(book)
        raise ValueError(f"Unknown display type: {display_type}")
