from abc import ABC, abstractmethod

from app.models import Book


class DefaultInterface(ABC):
    @abstractmethod
    def run(self, book: Book) -> None | str:
        pass
