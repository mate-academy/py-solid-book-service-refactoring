from abc import ABC, abstractmethod

from app.book_class import Book


class PrintStrategy(ABC):
    @staticmethod
    @abstractmethod
    def print(book: Book) -> None:
        pass


class ConsolePrint(PrintStrategy):
    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintStrategy):
    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
