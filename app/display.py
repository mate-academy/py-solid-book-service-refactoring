from abc import ABC, abstractmethod
from app.models import Book


class DisplayABC(ABC):
    @abstractmethod
    def display(self, book: "Book"):
        pass


class DisplayConsole(DisplayABC):
    def display(self, book: "Book"):
        print(book.content)



class DisplayReverse(DisplayABC):
    def display(self, book: "Book") -> None:
        print(book.content[::-1])

