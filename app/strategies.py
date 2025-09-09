from abc import ABC, abstractmethod
from .models import Book


class DisplayStrategy(ABC):
    @abstractmethod
    def render(self, book: Book) -> str:
        pass


class ConsoleDisplay(DisplayStrategy):
    def render(self, book: Book) -> str:
        return book.content


class ReverseDisplay(DisplayStrategy):
    def render(self, book: Book) -> str:
        return book.content[::-1]
