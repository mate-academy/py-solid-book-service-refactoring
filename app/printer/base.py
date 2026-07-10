from abc import ABC, abstractmethod

from app.book import Book


class BasePrinter(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass
