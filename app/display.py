from abc import ABC, abstractmethod
from app.book import Book


class DisplayCMD(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayCMD):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayCMD):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


display_handlers = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}
