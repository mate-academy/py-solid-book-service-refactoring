from abc import ABC, abstractmethod

from app.book import Book


class PrintType(ABC, Book):
    @abstractmethod
    def print(self):
        pass


class PrintConsole(PrintType):
    def print(self):
        print(f"Printing the book: {self.title}...")
        print(self.content)


class PrintReverse(PrintType):
    def print(self):
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])
