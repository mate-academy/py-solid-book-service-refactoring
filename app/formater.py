from abc import ABC, abstractmethod

from app.book import Book


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class NormalFormat(Formatter):
    def format(self, book: Book) -> str:
        return book.content


class ReverseFormat(Formatter):
    def format(self, book: Book) -> str:
        return book.content[::-1]
