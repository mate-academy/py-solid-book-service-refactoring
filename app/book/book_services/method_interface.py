from abc import ABC, abstractmethod
from app.book.book import Book
from typing import Optional


class IBookAction(ABC):
    @staticmethod
    @abstractmethod
    def method(book: Book) -> Optional[str]:
        pass
