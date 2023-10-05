from abc import ABC, abstractmethod

from app.book import Book


class Print(ABC):
    @abstractmethod
    def do_action(self) -> None:
        pass


class PrintConsole(Print):
    def __init__(self, book: Book) -> None:
        self.content = book.content
        self.title = book.title

    def do_action(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)


class PrintReverse(Print):
    def __init__(self, book: Book) -> None:
        self.content = book.content
        self.title = book.title

    def do_action(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])
