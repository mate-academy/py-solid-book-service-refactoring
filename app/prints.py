from abc import ABC, abstractmethod

from app.book import Book


class BookPrint(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        ...


class ConsolePrint(BookPrint):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(BookPrint):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
