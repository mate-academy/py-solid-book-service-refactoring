from abc import ABC, abstractmethod

from app.models import Book


class BookDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class BookPrint(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class BookSerialize(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass
