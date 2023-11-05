from abc import ABC, abstractmethod

from app.book import Book


class PrintBook(ABC):
    @abstractmethod
    def print_book(self) -> None:
        pass


class PrintBookConsole(PrintBook):
    def __init__(self, book: Book) -> None:
        self.content = book.content
        self.method_type = "console"
        self.message = f"Printing the book: {book.title}..."

    def print_book(self) -> None:
        print(self.message)
        print(self.content)


class PrintBookReverse(PrintBook):
    def __init__(self, book: Book) -> None:
        self.content = book.content
        self.method_type = "reverse"
        self.message = f"Printing the book in reverse: {book.title}..."

    def print_book(self) -> None:
        print(self.message)
        print(self.content[::-1])
