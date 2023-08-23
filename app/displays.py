from abc import abstractmethod, ABC

from app.models import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        ...


class ConsoleDisplay(Display):

    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(Display):

    def display(self, book: Book) -> None:
        print(book.content[::-1])
