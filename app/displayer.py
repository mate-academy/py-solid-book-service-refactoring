from abc import ABC, abstractmethod

from app.book_model import Book


class BookDisplayer(ABC):
    @staticmethod
    @abstractmethod
    def display_book(book: Book) -> None:
        pass


class ConsoleDisplayer(BookDisplayer):
    @staticmethod
    def display_book(book: Book) -> None:
        print(book.content)


class ReverseDisplayer(BookDisplayer):
    @staticmethod
    def display_book(book: Book) -> None:
        print(book.content[::-1])
