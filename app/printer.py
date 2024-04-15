from abc import ABC, abstractmethod

from app.book import Book


class BookPrinter(ABC):

    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsoleBookPrinter(BookPrinter):

    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReverseBookPrinter(BookPrinter):

    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


def create_book_printer(print_type: str) -> BookPrinter:

    if print_type == "console":
        return ConsoleBookPrinter()
    elif print_type == "reverse":
        return ReverseBookPrinter()
    raise ValueError(f"Unknown print type: {print_type}")
