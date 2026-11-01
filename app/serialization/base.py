from abc import ABC, abstractmethod

from app.book import Book


class SerializeBook(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass
