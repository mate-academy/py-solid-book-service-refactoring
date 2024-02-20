from abc import ABC, abstractmethod

from app.book import Book


class ServiceCommands(ABC):
    @abstractmethod
    def console(self, book: Book) -> None:
        pass

    @abstractmethod
    def reverse(self, book: Book) -> None:
        pass


class DisplayCommands(ServiceCommands):
    def console(self, book: Book) -> None:
        print(book.content)

    def reverse(self, book: Book) -> None:
        print(book.content[::-1])


class PrintCommands(ServiceCommands):
    def console(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)

    def reverse(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
