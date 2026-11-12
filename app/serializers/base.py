from abc import ABC, abstractmethod

from app.models import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass
