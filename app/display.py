from abc import ABC, abstractmethod

from app.book import Book


class DisplayBook(ABC):
    @abstractmethod
    def display_book(self, book: Book) -> None:
        pass


class DisplayBookConsole(DisplayBook):
    def display_book(self, book: Book) -> None:
        print(book.content)


class DisplayBookReverse(DisplayBook):
    def display_book(self, book: Book) -> None:
        print(book.content[::-1])


class PrintBook(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class PrintBookConsole(PrintBook):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...\n{book.content}")


class PrintBookReverse(PrintBook):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}..."
              f"\n{book.content[::-1]}")
