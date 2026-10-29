from abc import ABC, abstractmethod
from app.models.book import Book


class PrintStrategy(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrintStrategy(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrintStrategy(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class PrintService:
    def __init__(self, strategy: PrintStrategy) -> None:
        self.strategy = strategy

    def print_book(self, book: Book) -> None:
        self.strategy.print_book(book)


class PrintStrategyFactory:
    @staticmethod
    def create(strategy_type: str) -> PrintStrategy:
        strategies = {
            "console": ConsolePrintStrategy,
            "reverse": ReversePrintStrategy,
        }
        strategy_class = strategies.get(strategy_type)
        if strategy_class is None:
            raise ValueError(f"Unknown print type: {strategy_type}")
        return strategy_class()
