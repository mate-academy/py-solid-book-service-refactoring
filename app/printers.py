from __future__ import annotations
from abc import ABC, abstractmethod

from app.book import Book


class IPrinter(ABC):
    _registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        IPrinter._registry[cls.__name__.lower()] = cls

    @classmethod
    def get_printer(cls, method_type) -> IPrinter:
        if method_type not in IPrinter._registry:
            raise ValueError(f"Unknown printer type: {method_type}")
        return IPrinter._registry[method_type]()

    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class Console(IPrinter):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class Reverse(IPrinter):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
