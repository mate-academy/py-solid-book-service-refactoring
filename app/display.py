from abc import ABC, abstractmethod

from app.book import Book


class Display(ABC):
    @abstractmethod
    def do_action(self) -> None:
        pass


class DisplayConsole(Display):
    def __init__(self, book: Book) -> None:
        self.content = book.content

    def do_action(self) -> None:
        print(self.content)


class DisplayReverse(Display):
    def __init__(self, book: Book) -> None:
        self.content = book.content

    def do_action(self) -> None:
        print(self.content[::-1])
