from abc import ABC, abstractmethod

from app.book import Book


class PrintBook(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class PrintBookConsole(PrintBook):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...\n{book.content}")


class PrintBookReverse(PrintBook):
    def print(self, book: Book) -> None:
        print(
            f"Printing the book in reverse: "
            f"{book.title}...\n{book.content[::-1]}"
        )
