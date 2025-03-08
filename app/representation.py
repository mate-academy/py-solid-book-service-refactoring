from abc import ABC, abstractmethod
from app.book import Book


class TypeOfRepresentation(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        ...

    @abstractmethod
    def print_book(self, book: Book) -> None:
        ...


class ConsoleRepresentation(TypeOfRepresentation):
    def display(self, book: Book) -> None:
        print(book.content)

    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReverseRepresentation(TypeOfRepresentation):
    def display(self, book: Book) -> None:
        print(book.content[::-1])

    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
