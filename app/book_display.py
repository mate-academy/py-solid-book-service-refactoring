from abc import ABC, abstractmethod

from app.book import Book


class DisplayType(ABC):
    @abstractmethod
    def display(self, book: Book):
        pass


class DisplayConsole(DisplayType):
    def display(self, book: Book):
        print(book.content)


class DisplayReverse(DisplayType):
    def display(self, book: Book):
        print(book.content[::-1])
