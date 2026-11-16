from abc import ABC, abstractmethod

from app.models import Book


class BookDisplayInterface(ABC):
    @abstractmethod
    def display(self, book: Book) -> str:
        pass


class DetailBookInterface(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> str:
        pass


class SerializeBookInterface(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass
