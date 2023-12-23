from abc import abstractmethod, ABC

from app.book_model import Book


class BookPrinter(ABC):
    @staticmethod
    @abstractmethod
    def print_book(book: Book) -> None:
        pass


class ConsolePrinter(BookPrinter):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(BookPrinter):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
