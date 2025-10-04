from abc import ABC, abstractmethod

from app.books import Book


class Display(ABC):

    @abstractmethod
    def display(self, data: str) -> None:
        pass


class ConsoleDisplay(Display):

    def display(self, data: str) -> None:
        print(data)


class ReverseDisplay(Display):

    def display(self, data: str) -> None:
        print(data[::-1])


class BookDisplay:

    def __init__(self, display: Display) -> None:
        self.display = display

    def display_book(self, book: Book) -> None:
        self.display.display(book.content)
