from abc import ABC, abstractmethod

from app.book import Book


class Print(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def exec(self) -> None:
        pass


class PrintConsole(Print):
    def exec(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class PrintReverse(Print):
    def exec(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])


print_handlers = {
    "reverse": PrintReverse,
    "console": PrintConsole
}
