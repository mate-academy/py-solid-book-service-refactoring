from abc import ABC, abstractmethod

from app.book_model import Book


class IBookDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class IBookPrint(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class IBookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass
