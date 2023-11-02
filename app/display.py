import abc

from app.book import Book


class Display(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def display(book: Book) -> None:
        ...


class DisplayConsole(Display):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content)


class DisplayReverse(Display):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])
