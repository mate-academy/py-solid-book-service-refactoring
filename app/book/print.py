from abc import abstractmethod, ABC

from app.book.book import Book


class Print(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class PrintConsole(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
