import abc

from app.book import Book


class PrintBook(abc.ABC):
    def __init__(self, book: Book):
        self.book = book

    @abc.abstractmethod
    def print_book(self) -> None:
        pass


class PrintConsole(PrintBook):
    def print_book(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class PrintReverse(PrintBook):
    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])
