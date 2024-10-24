from abc import ABC, abstractmethod
from app.book import Book


class DisplayStrategy(ABC):

    @abstractmethod
    def display(self, book: Book) -> str:
        pass


class ConsoleDisplayStrategy(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayStrategy(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class DisplayStrategyHandler:
    def __init__(
            self,
            console_display: DisplayStrategy,
            reverse_display: DisplayStrategy
    ) -> None:
        self.console_display = console_display
        self.reverse_display = reverse_display

    def display(self, book: Book, display_type: str) -> str:
        if display_type == "console":
            return self.console_display.display(book)
        elif display_type == "reverse":
            return self.reverse_display.display(book)
        else:
            raise ValueError(f"Unknown display type: {display_type}")
