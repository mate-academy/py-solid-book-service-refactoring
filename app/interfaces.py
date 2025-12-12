from abc import ABC, abstractmethod

from .models import Book


class IDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class IPrinter(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ISerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass
