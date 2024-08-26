from abc import abstractmethod, ABC

from app.book import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(Display):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseConsoleDisplay(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
