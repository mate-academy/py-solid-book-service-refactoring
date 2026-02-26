from abc import ABC, abstractmethod

from app.book import Book
from app.formater import Formatter


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(Display):
    def __init__(self, formatter: Formatter) -> None:
        self.formatter = formatter

    def display(self, book: Book) -> None:
        text = self.formatter.format(book)
        print(text)
