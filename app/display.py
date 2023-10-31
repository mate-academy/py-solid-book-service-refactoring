from abc import ABC, abstractmethod

from app.book import Book


class Display(ABC):
    @staticmethod
    @abstractmethod
    def exec(book: Book) -> None:
        pass


class DisplayConsole(Display):
    @staticmethod
    def exec(book: Book) -> None:
        print(book.content)


class DisplayReverse(Display):
    @staticmethod
    def exec(book: Book) -> None:
        print(book.content[::-1])


display_handlers = {
    "reverse": DisplayReverse(),
    "console": DisplayConsole()
}
