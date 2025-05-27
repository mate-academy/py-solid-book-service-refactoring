from abc import ABC, abstractmethod

from app.books import Book


class BookPrinter(ABC):

    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrinter(BookPrinter):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(BookPrinter):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class DummyPrinter(BookPrinter):
    def print_book(self, book: Book) -> None:
        pass
