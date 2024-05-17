from abc import ABC, abstractmethod

from app.book import Book


class DisplayBook(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


class DisplayConsole(DisplayBook):
    def __init__(self, book: Book) -> None:
        self.content = book.content

    def display(self) -> None:
        print(self.content)


class DisplayReverse(DisplayBook):
    def __init__(self, book: Book) -> None:
        self.content = book.content

    def display(self) -> None:
        print(self.content[::-1])
