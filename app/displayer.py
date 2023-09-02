from abc import ABC, abstractstaticmethod


class BookDisplayer(ABC):
    @abstractstaticmethod
    def display(book):
        pass


class ConsoleBookDisplayer(BookDisplayer):
    @staticmethod
    def display(book):
        print(book.content)


class ReverseBookDisplayer(BookDisplayer):
    @staticmethod
    def display(book):
        print(book.content[::-1])
