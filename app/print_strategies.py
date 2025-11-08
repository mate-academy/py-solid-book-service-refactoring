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


class PrintStrategyFactory:
    @staticmethod
    def get_strategy(print_type: str) -> PrintStrategy:
        if print_type == "console":
            return ConsolePrint()
        elif print_type == "reverse":
            return ReversePrint()
        else:
            raise ValueError(f"Unknown print type: {print_type}")
