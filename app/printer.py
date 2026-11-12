from abc import ABC, abstractmethod

from app.book import Book


class Printer(ABC):
    @abstractmethod
    def print_book(self, book: Book, show_title: bool) -> None:
        pass


class ConsolePrinter(Printer):
    def print_book(self, book: Book, show_title: bool) -> None:
        if show_title:
            print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(Printer):
    def print_book(self, book: Book, show_title: bool) -> None:
        if show_title:
            print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
