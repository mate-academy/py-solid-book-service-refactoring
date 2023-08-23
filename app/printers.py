from abc import abstractmethod, ABC

from app.models import Book


class Printer(ABC):

    @abstractmethod
    def print(self, book: Book) -> None:
        ...


class PrintBook(Printer):

    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintRevers(Printer):

    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
