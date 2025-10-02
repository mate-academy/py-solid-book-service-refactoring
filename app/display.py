from abc import ABC, abstractmethod

from app.book import Book, IBook


class IDisplay(ABC):
    @abstractmethod
    def display(self, book: IBook) -> None:
        pass


class DisplayConsole(IDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayReverse(IDisplay):
    def display(self, book: IBook) -> None:
        print(book.content[::-1])
