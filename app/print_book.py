from abc import ABC, abstractmethod

from app.book import Book


class BasePrint(ABC):
    @abstractmethod
    def print_book(self, print_type: str) -> None:
        pass


class ConsolePrint(BasePrint):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(BasePrint):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
