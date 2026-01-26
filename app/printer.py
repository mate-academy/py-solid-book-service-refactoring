from abc import ABC, abstractmethod

from app.book import Book


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class ConsoleFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content


class ReverseFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content[::-1]


class DetailedPrinter(Formatter):
    def format(self, book: Book) -> str:
        return f"Printing the book: {book.title}...\n{book.content}"


class ReverseDetailedPrinter(Formatter):
    def format(self, book: Book) -> str:
        return (f"Printing the book in reverse: "
                f"{book.title}...\n{book.content[::-1]}")
