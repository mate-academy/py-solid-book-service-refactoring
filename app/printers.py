from abc import abstractmethod, ABC

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
