from abc import ABC, abstractmethod
from app.models.models import Book


class SerializerStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass
