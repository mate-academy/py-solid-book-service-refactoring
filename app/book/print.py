from abc import ABC, abstractmethod

from app.book.book import Book


class Print(ABC):
    @abstractmethod
    def print(self, book: Book):
        pass


class PrintConsole(Print):
    def print(self, book: Book):
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(Print):
    def print(self, book: Book):
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])