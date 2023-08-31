from abc import ABC, abstractmethod

from app.book import Book


class BookPrinter(ABC):

    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrinter(BookPrinter):

    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.get_title()}...")
        print(book.get_content())


class ReversePrinter(BookPrinter):

    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.get_title()}...")
        print(book.get_content()[::-1])
