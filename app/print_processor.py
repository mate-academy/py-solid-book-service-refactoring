from abc import ABC, abstractmethod

from app.book import Book


class PrintProcessor(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class PrintConsoleProcessor(PrintProcessor):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverseProcessor(PrintProcessor):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
