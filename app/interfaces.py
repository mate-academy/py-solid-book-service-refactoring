from abc import ABC, abstractmethod

from app.book import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ShowBookDetail(ABC):
    @abstractmethod
    def show(self, book: Book) -> None:
        pass


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass
