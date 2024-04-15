from abc import ABC, abstractmethod

from app.book import Book


class Display(ABC):

    @abstractmethod
    def display(self) -> None:
        pass


class ConsoleDisplay(Display):

    def __init__(self, book: Book) -> None:
        self.content = book.content

    def display(self) -> None:
        print(self.content)


class ReverseDisplay(Display):

    def __init__(self, book: Book) -> None:
        self.content = book.content

    def display(self) -> None:
        print(self.content[::-1])
