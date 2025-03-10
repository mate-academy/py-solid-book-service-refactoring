from abc import ABC, abstractmethod
from app.book import Book


class AbstractDisplayService(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplayService(AbstractDisplayService):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayService(AbstractDisplayService):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
