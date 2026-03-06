from abc import ABC, abstractmethod
from app.models import Book


class BookAction(ABC):
    @abstractmethod
    def execute(self, book: Book) -> str | None:
        pass


class DisplayInterface(BookAction):
    @abstractmethod
    def execute(self, book: Book) -> None:
        pass


class PrinterInterface(BookAction):
    @abstractmethod
    def execute(self, book: Book) -> None:
        pass


class SerializerInterface(BookAction):
    @abstractmethod
    def execute(self, book: Book) -> str:
        pass
