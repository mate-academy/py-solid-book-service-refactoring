from abc import ABC, abstractmethod

from book.book import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class DisplayConsole(Display):
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayReverse(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
