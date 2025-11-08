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


class DisplayStrategyFactory:
    @staticmethod
    def get_strategy(display_type: str) -> DisplayStrategy:
        if display_type == "console":
            return ConsoleDisplay()
        elif display_type == "reverse":
            return ReverseDisplay()
        else:
            raise ValueError(f"Unknown display type: {display_type}")
