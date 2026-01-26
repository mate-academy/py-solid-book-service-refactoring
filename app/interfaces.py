from abc import ABC, abstractmethod
from app.book import Book


class IWriter(ABC):
    @abstractmethod
    def write(self, text: str) -> None:
        pass


class IDisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class IPrintStrategy(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ISerializerStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass
