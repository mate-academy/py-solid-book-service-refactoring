from abc import ABC, abstractmethod

from .display import DisplayConsole, DisplayReverse


class Print(ABC):
    @abstractmethod
    def print_book(self, title, content) -> None:
        pass


class PrintConsole(Print, DisplayConsole):
    def print_book(self, title, content) -> None:
        print(f"Printing the book: {title}...")
        self.display(content)


class PrintReverse(Print, DisplayReverse):
    def print_book(self, title, content) -> None:
        print(f"Printing the book in reverse: {title}...")
        self.display(content)
