from abc import abstractmethod, ABC

from book.book import Book


class Printer(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class PrinterConsole(Printer):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrinterReverse(Printer):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
