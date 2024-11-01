from abc import ABC, abstractmethod
from typing import Any


class Display(ABC):
    @abstractmethod
    def display_type(self, book: Any) -> None:
        pass


class DisplayConsole(Display):
    def display_type(self, book: Any) -> None:
        print(book.content)


class DisplayReverse(Display):
    def display_type(self, book: Any) -> None:
        print(book.content[::-1])
