from abc import ABC, abstractmethod

from app.models import Book


class DisplayInterface(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class SerializeInterface(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass
