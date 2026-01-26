from abc import ABC, abstractmethod
from app.interfaces import HasContent


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: HasContent) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: HasContent) -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book: HasContent) -> None:
        print(book.content[::-1])
