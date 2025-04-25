from abc import ABC, abstractmethod
from app.book import Book


class PrintBook(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class PrintReverse(PrintBook):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class PrintConsole(PrintBook):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)
