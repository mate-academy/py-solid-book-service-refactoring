from abc import ABC, abstractmethod

from app.book import Book


class DisplayBook(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


class DisplayBookConsole(DisplayBook):

    def __init__(self, book: Book) -> None:
        self.content = book.content
        self.method_type = "console"

    def display(self) -> None:
        print(self.content)


class DisplayBookReverse(DisplayBook):

    def __init__(self, book: Book) -> None:
        self.content = book.content
        self.method_type = "reverse"

    def display(self) -> None:
        print(self.content[::-1])
