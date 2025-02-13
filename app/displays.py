from abc import abstractmethod, ABC

from app.book import Book


class DisplayMethod(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayMethod):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayMethod):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
