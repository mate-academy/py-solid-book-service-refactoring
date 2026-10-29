from abc import ABC, abstractmethod

from app.book import Book


class BookPrinter(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        ...


class ConsolePrinter(BookPrinter):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(BookPrinter):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
