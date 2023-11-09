from abc import ABC, abstractmethod

from app.book import Book


class PrintBook(ABC):
    method_type = None

    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def print_book(self) -> None:
        pass


class PrintBookConsole(PrintBook):
    method_type = "console"

    def print_book(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class PrintBookReverse(PrintBook):
    method_type = "reverse"

    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])


def print_manager(method: str, book: Book) -> None:
    for subclass in PrintBook.__subclasses__():
        print(subclass.method_type)
        if subclass.method_type == method:
            selected_class = subclass(book=book)
            if selected_class is None:
                raise ValueError(f"Unknown print type: {method}")
            selected_class.print_book()
