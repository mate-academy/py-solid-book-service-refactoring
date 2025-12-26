from abc import abstractmethod, ABC

from app.models import Book


class Display(ABC):
    pass

    @abstractmethod
    def show(self, book: Book) -> None:
        pass


class ConsoleDisplay(Display):
    def show(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(Display):
    def show(self, book: Book) -> None:
        print(book.content[::-1])
