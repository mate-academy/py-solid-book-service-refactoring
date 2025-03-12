from abc import ABC, abstractmethod

from app.models import Book


class DisplayBookInterface(ABC):
    @abstractmethod
    def display_book(self, book: Book) -> None:
        pass


class PrintBookInterface(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class SerializerBookInterface(ABC):
    @abstractmethod
    def serializer_book(self, book: Book) -> str:
        pass
