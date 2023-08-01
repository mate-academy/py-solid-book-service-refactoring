from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayBook(ABC):
    display_method = ["console", "reverse"]

    @staticmethod
    @abstractmethod
    def display(book: Book) -> None:
        pass


class ConsoleDisplay(DisplayBook):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayBook):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])


class PrintBook(ABC):
    print_method = ["console", "reverse"]

    @staticmethod
    @abstractmethod
    def print_book(book: Book) -> None:
        pass


class ConsolePrint(PrintBook):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintBook):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
