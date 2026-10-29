from abc import ABC, abstractmethod
from app.models.book import Book


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplayStrategy(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayStrategy(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class DisplayService:
    def __init__(self, strategy: DisplayStrategy) -> None:
        self.strategy = strategy

    def display(self, book: Book) -> None:
        self.strategy.display(book)


class DisplayStrategyFactory:
    @staticmethod
    def create(strategy_type: str) -> DisplayStrategy:
        strategies = {
            "console": ConsoleDisplayStrategy,
            "reverse": ReverseDisplayStrategy,
        }
        strategy_class = strategies.get(strategy_type)
        if strategy_class is None:
            raise ValueError(f"Unknown display type: {strategy_type}")
        return strategy_class()
