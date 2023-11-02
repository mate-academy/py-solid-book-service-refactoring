import abc

from app.book import Book


class DisplayBook(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def display(book: Book) -> None:
        pass


class DisplayConsole(DisplayBook):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content)


class DisplayReverse(DisplayBook):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])
