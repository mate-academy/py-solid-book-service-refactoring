from abc import ABC, abstractmethod
from app.model import Book


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class PrintStrategy(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class Serialize(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass
