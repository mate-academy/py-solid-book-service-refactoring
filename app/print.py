from abc import abstractmethod, ABC

from .book import Book


class Printer(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrinter(Printer):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(Printer):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class BookPrinter:
    @staticmethod
    def print_book(book: Book, print_type: str) -> None:
        if print_type == "console":
            ConsolePrinter().print_book(book)
        elif print_type == "reverse":
            ReversePrinter().print_book(book)
        else:
            raise ValueError(f"Unknown print type: {print_type}")
