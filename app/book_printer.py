from abc import ABC, abstractmethod
from app.book import Book


class BookPrintContentDisplay(ABC):

    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrintContentDisplay(BookPrintContentDisplay):

    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrintContentDisplay(BookPrintContentDisplay):

    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
