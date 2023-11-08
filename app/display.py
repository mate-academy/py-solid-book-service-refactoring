import abc

from app.book import Book


class DisplayBook(abc.ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abc.abstractmethod
    def display(self) -> None:
        pass


class DisplayConsole(DisplayBook):
    def display(self) -> None:
        print(self.book.content)


class DisplayReverse(DisplayBook):
    def display(self) -> None:
        print(self.book.content[::-1])
