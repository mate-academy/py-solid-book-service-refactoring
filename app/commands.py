from abc import ABC, abstractmethod
from app.book import Book
from app.strategies import (
    DisplayStrategy,
    PrintStrategy,
    SerializationStrategy
)


class Command(ABC):
    @abstractmethod
    def execute(self) -> None | str:
        pass


class DisplayCommand(Command):
    def __init__(self, book: Book, display_strategy: DisplayStrategy) -> None:
        self.book = book
        self.display_strategy = display_strategy

    def execute(self) -> None:
        self.display_strategy.display(self.book)


class PrintCommand(Command):
    def __init__(self, book: Book, print_strategy: PrintStrategy) -> None:
        self.book = book
        self.print_strategy = print_strategy

    def execute(self) -> None:
        self.print_strategy.print_book(self.book)


class SerializeCommand(Command):
    def __init__(
            self,
            book: Book,
            serialization_strategy: SerializationStrategy
    ) -> None:
        self.book = book
        self.serialization_strategy = serialization_strategy

    def execute(self) -> str:
        return self.serialization_strategy.serialize(self.book)
