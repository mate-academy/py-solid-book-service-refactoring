from abc import ABC, abstractmethod

from app.models import Book


class PrintServiceBase(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrintService(PrintServiceBase):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrintService(PrintServiceBase):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


def get_book_print_type(print_type: str) -> PrintServiceBase:
    if print_type == "console":
        return ConsolePrintService()
    elif print_type == "reverse":
        return ReversePrintService()
    else:
        raise ValueError(f"Unknown print type: {print_type}")
