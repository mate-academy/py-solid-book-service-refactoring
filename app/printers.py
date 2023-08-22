from abc import abstractmethod

from app.book import Book


class Printer:
    @abstractmethod
    def perform_print(self, book: Book) -> None:
        pass


class ConsolePrinter(Printer):
    def perform_print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(Printer):
    def perform_print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
