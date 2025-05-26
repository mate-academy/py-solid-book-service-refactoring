from abc import ABC, abstractmethod

from app.book import Book


class IBookDisplayer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def display(self) -> None:
        pass


class ConsoleBookDisplayer(IBookDisplayer):
    def display(self) -> None:
        print(self.book.content)


class ReverseBookDisplayer(IBookDisplayer):
    def display(self) -> None:
        print(self.book.content[::-1])


def select_displayer(method_type: str) -> type[IBookDisplayer]:
    displayers = {
        "console": ConsoleBookDisplayer,
        "reverse": ReverseBookDisplayer,
    }

    return displayers[method_type]
