from abc import ABC, abstractmethod

from app.book import Book


class PrintType(ABC, Book):
    @abstractmethod
    def print(self, book: Book):
        pass


class PrintConsole(PrintType):
    def print(self, book: Book):
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(PrintType):
    def print(self, book: Book):
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
