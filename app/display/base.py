from abc import ABC, abstractmethod

from app.book import Book


class Display(ABC):
    @abstractmethod
    def display_content(self, book: "Book") -> None:
        pass
