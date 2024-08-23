from abc import abstractmethod, ABC

from app.book import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class DisplayConsole(Display):
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayConsoleReverse(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
