from abc import ABC, abstractstaticmethod


class BookPrinter(ABC):
    @abstractstaticmethod
    def print(book):
        pass


class ConsoleBookPrinter(BookPrinter):
    @staticmethod
    def print(book):
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReverseBookPrinter(BookPrinter):
    @staticmethod
    def print(book):
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
