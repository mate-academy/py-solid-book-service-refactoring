from abc import ABC, abstractmethod

from app.book import Book


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class ConsolFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content


class ReverseFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content[::-1]
