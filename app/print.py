from abc import ABC, abstractmethod

from app.books import Book


class PrintService(ABC):
    @staticmethod
    @abstractmethod
    def print(book: Book) -> None:
        pass


class ConsolePrintService(PrintService):

    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrintService(PrintService):
    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
