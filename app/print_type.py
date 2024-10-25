from abc import ABC, abstractmethod

from app.book import Book


class BasePrintType(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        ...


class ConsolePrint(BasePrintType):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(BasePrintType):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
