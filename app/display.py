from abc import ABC, abstractmethod

from app.book import Book


class Display(ABC):
    @staticmethod
    def display(book):
        pass


class ConsoleDisplay(Display):
    @staticmethod
    def display(book):
        print(book.content)


class ReverseDisplay(Display):
    @staticmethod
    def display(book):
        print(book.content[::-1])
