from abc import ABC, abstractmethod

from app.entities.book import Book


class BaseDisplayer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def display(self) -> None:
        pass


class ConsoleDisplayer(BaseDisplayer):
    def display(self) -> None:
        print(self.book.content)


class ReverseDisplayer(BaseDisplayer):
    def display(self) -> None:
        print(self.book.content[::-1])
