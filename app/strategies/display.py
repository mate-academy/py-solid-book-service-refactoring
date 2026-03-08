from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.book import Book


class DisplayStrategy:
    def display(self, book: "Book") -> None:
        raise NotImplementedError


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: "Book") -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book: "Book") -> None:
        print(book.content[::-1])


display_strategies = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}
