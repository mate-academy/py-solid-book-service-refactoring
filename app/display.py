from abc import ABC, abstractmethod

from app.book import Book


class Display(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        ...

    @abstractmethod
    def print_book(self, book: Book) -> None:
        ...


class ConsoleDisplay(Display):
    def display(self, book: Book) -> None:
        print(book.content)

    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        self.display(book)


class ReverseDisplay(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])

    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        self.display(book)
