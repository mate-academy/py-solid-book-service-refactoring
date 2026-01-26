from abc import ABC, abstractmethod
from app.models.book import Book


class Command(ABC):
    @abstractmethod
    def execute(self, book: Book):
        pass
