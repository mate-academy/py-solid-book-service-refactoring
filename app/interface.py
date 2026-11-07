from abc import ABC, abstractmethod
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.main import Book


class DisplayInterface(ABC):
    @abstractmethod
    def display(self, book: "Book") -> None:
        pass


class PrintInterface(ABC):
    @abstractmethod
    def print_book(self, book: "Book") -> None:
        pass


class SerializeInterface(ABC):
    @abstractmethod
    def serialize(self, book: "Book") -> str:
        pass
