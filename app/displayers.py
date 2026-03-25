from app.models import Book
from typing import Protocol
from abc import abstractmethod


class DisplayServiceProtocol(Protocol):
    @abstractmethod
    def console(self, book: Book) -> None:
        ...

    @abstractmethod
    def reverse(self, book: Book) -> None:
        ...


class PrintServiceProtocol(Protocol):
    @abstractmethod
    def console(self, book: Book) -> None:
        ...

    @abstractmethod
    def reverse(self, book: Book) -> None:
        ...


class DisplayService(DisplayServiceProtocol):
    def __init__(self) -> None:
        pass

    def console(self, book: Book) -> None:
        print(book.content)

    def reverse(self, book: Book) -> None:
        print(book.content[::-1])


class PrintService(PrintServiceProtocol):
    def __init__(self, display_service: DisplayServiceProtocol) -> None:
        self.display_service = display_service

    def console(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        self.display_service.console(book)

    def reverse(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        self.display_service.reverse(book)
