from abc import ABC, abstractmethod
from app.book import Book


class Printer(ABC):
    @abstractmethod
    def print_book(self, book: "Book") -> None:
        pass
