from abc import ABC, abstractmethod

from .display import DisplayConsole, DisplayReverse


class Print(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class PrintConsole(Print, DisplayConsole):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        self.display(content)


class PrintReverse(Print, DisplayReverse):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        self.display(content)
