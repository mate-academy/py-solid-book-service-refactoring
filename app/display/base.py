from abc import ABC, abstractmethod
from app.models import Book


class DisplayBook(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass
