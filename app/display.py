from abc import ABC, abstractmethod

from app.book import Book


class Display(ABC):
    def __init__(self, book: Book):
        self.book = book

    @abstractmethod
    def display(self, message: str):
        pass


class ConsoleDisplay(Display):
    def display(self, message: str):
        print(self.book.content)


class ReverseDisplay(Display):
    def display(self, message: str):
        print(self.book.content[::-1])
