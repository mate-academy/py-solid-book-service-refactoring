from abc import ABC, abstractmethod
from app.models import Book


class PrintBook(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass
