from typing import Protocol

from app.book import Book


class PrintStrategy(Protocol):
    def print_book(self, book: Book) -> None:
        ...


class ConsolePrint:
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint:
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
