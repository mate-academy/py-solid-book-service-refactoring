from typing import Protocol

from app.models import Book


class BookDisplay(Protocol):
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay:
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay:
    def display(self, book: Book) -> None:
        print(book.content[::-1])


DISPLAYERS: dict[str, BookDisplay] = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}
