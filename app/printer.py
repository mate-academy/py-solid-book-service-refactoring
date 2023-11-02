from abc import ABC, abstractmethod


class Printer(ABC):

    @staticmethod
    def print(book):
        pass


class ConsolePrinter(Printer):
    @staticmethod
    def print(book):
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(Printer):
    @staticmethod
    def print(book):
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
