from abc import ABC, abstractmethod

from . import BookABC


class Display(ABC):
    @staticmethod
    @abstractmethod
    def display(book: BookABC) -> None:
        pass


class DisplayToConsole(Display):
    @staticmethod
    def display(book: BookABC) -> None:
        print(book.content)


class DisplayInReverse(Display):
    @staticmethod
    def display(book: BookABC) -> None:
        print(book.content[::-1])
