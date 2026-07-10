from abc import ABC, abstractmethod

from app.book import Book


class BaseSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass
