from abc import ABC, abstractmethod
from app.models.book import Book


class Printer(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass
