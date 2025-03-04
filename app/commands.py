from abc import ABC, abstractmethod

from app.models import Book


class Representation(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleRepresentation(Representation):
    def display(self, book: Book) -> None:
        print(book.content)

    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        self.display(book)


class ReverseRepresentation(Representation):
    def display(self, book: Book) -> None:
        print(book.content[::-1])

    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        self.display(book)
