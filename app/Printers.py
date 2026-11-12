from abc import ABC, abstractmethod

from app.Displayers import Displayer
from app.Models import Book


class Printer(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class HeaderPrinter(Printer):
    """Друкує заголовок, вміст делегує Displayer."""

    def __init__(self, header_template: str, displayer: Displayer) -> None:
        self._header_template = header_template
        self._displayer = displayer

    def print_book(self, book: Book) -> None:
        print(self._header_template.format(title=book.title))
        self._displayer.display(book)
