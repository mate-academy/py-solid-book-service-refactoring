from abc import ABC, abstractmethod

from app.book.book import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: Book):
        pass


class DisplayConsole(Display):
    def display(self, book: Book):
        print(book.content)


class DisplayReverse(Display):
    def display(self, book: Book):
        print(book.content[::-1])
