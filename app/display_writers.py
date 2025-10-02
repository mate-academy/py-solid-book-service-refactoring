from __future__ import annotations
from abc import abstractmethod, ABC

from app.book import Book


class IDisplayWriter(ABC):
    _registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        IDisplayWriter._registry[cls.__name__.lower()] = cls

    @classmethod
    def get_display(cls, method_type) -> IDisplayWriter:
        if method_type not in IDisplayWriter._registry:
            raise ValueError(f"Unknown display type: {method_type}")
        return IDisplayWriter._registry[method_type]()

    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class Console(IDisplayWriter):
    def display(self, book: Book) -> None:
        print(book.content)


class Reverse(IDisplayWriter):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
