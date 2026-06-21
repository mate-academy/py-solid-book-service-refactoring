from abc import ABC, abstractmethod

from app.models.book import Book


class Displayer(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass
