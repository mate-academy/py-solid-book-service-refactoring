from abc import ABC, abstractmethod
from app.book import Book


class BookContentDisplay(ABC):

    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleContentDisplay(BookContentDisplay):

    def display(self, book: Book) -> None:
        print(book.content)


class ReverseContentDisplay(BookContentDisplay):

    def display(self, book: Book) -> None:
        print(book.content[::-1])
