from abc import ABC, abstractmethod

from app.book import Book


class BookService(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def execute(self, method_type: str) -> None | str:
        pass
