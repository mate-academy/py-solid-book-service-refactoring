from abc import ABC, abstractmethod

from app.book import Book


class IBookService(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass

    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class BookServiceConsole(IBookService):
    def display(self, book: Book) -> None:
        print(book.content)

    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class BookServiceReverse(IBookService):
    def display(self, book: Book) -> None:
        print(book.content[::-1])

    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
