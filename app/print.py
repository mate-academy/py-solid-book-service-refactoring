from abc import ABC, abstractmethod
from typing import Any


class Print(ABC):
    @abstractmethod
    def print(self) -> None:
        pass


class PrintConsole(Print):
    def __init__(self, book: Any) -> None:
        self.book = book

    def print(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class PrintReverse(Print):
    def __init__(self, book: Any) -> None:
        self.book = book

    def print(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])
