from abc import abstractmethod, ABC

from app.book import Book


class PrintBook(ABC):
    print_method = ["console", "reverse"]

    @staticmethod
    @abstractmethod
    def print_book(book: Book) -> None:
        pass


class ConsolePrint(PrintBook):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintBook):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
