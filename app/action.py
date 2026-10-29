from abc import ABC, abstractmethod

from app.book import Book


class Action(ABC):
    @abstractmethod
    def action(self, book: Book) -> None | str:
        pass
