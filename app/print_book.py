from abc import abstractmethod, ABC

from app.book import Book


class PrintBook(ABC):

    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def print_book(self: Book) -> str:
        pass


class PrintConsole(PrintBook):

    def print_book(self: Book) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)


class PrintReverse(PrintBook):

    def print_book(self: Book) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])
