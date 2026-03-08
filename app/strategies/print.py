from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.book import Book


class PrintStrategy:
    def print_book(self, book: "Book") -> None:
        raise NotImplementedError


class ConsolePrint(PrintStrategy):
    def print_book(self, book: "Book") -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintStrategy):
    def print_book(self, book: "Book") -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


print_strategies = {
    "console": ConsolePrint(),
    "reverse": ReversePrint(),
}
