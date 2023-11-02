import abc

from app.book import Book

class PrintBook(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def print_book(book: Book) -> None:
        ...


class PrintConsole(PrintBook):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(PrintBook):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
