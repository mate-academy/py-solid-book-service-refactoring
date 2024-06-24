from abc import ABC, abstractmethod
from app.book import Book


class DisplayBook(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class DisplayConsole(DisplayBook):
    def display(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class DisplayReverse(DisplayBook):
    def display(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
