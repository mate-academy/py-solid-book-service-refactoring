from abc import abstractmethod

from app.book import Book


class Display:

    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def display(self) -> None:
        pass


class ConsoleDisplay(Display):

    def display(self) -> None:
        print(self.book.content)


class ReverseDisplay(Display):

    def display(self) -> None:
        print(self.book.content[::-1])
