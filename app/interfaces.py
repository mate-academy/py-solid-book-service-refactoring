from abc import ABC, abstractmethod
from app.models import Book


class ActionInterface(ABC):
    @abstractmethod
    def execute(self, book: Book) -> str | None:
        pass
