from __future__ import annotations

from abc import ABC, abstractmethod

from app.book import Book


class DisplayMixin(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayMixin):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayMixin):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
