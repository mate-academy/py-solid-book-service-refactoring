from abc import ABC, abstractmethod

from app.books_manager.books import Book


class BookOutput(ABC):
    @staticmethod
    @abstractmethod
    def display(book: Book) -> None:
        pass

    @staticmethod
    @abstractmethod
    def print_book(book: Book) -> None:
        pass


class BookConsoleOutput(BookOutput):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content)

    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class BookReverseOutput(BookOutput):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])

    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
