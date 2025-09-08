from abc import ABC, abstractmethod
from models.book import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass
