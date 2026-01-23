from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(Display):

    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(Display):

    def display(self, book: Book) -> None:
        print(book.content[::-1])


class AbstractPrinter(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrinter(AbstractPrinter):

    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(f"Content: {book.content}")


class ReversePrinter(AbstractPrinter):

    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(f"Content: {book.content[::-1]}")
