from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class Display(ABC):
    @abstractmethod
    def display_book(self, book: Book) -> None:
        pass


class Print(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass
