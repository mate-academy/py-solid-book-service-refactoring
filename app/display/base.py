from abc import ABC, abstractmethod
from app.models import Book


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass
